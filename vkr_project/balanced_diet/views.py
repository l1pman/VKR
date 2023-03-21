import random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import User_param_form, CalorieCalcForm, User_progress_form, User_prefs_form
from .models import *

# Create your views here.
def index(request):
    return render(request, 'balanced_diet/index.html')

def try_service(request):
    if request.method == 'POST':
        form = CalorieCalcForm(request.POST)
        context = {'form': form}
        if form.is_valid():

            gender = form.cleaned_data.get('gender')
            weight = form.cleaned_data.get('weight')
            height = form.cleaned_data.get('height')
            age = form.cleaned_data.get('age')
            activity = form.cleaned_data.get('activity')

            if gender == 'M':
                kcal_value = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) \
                             * float(activity.replace(',', '.'))
            elif gender == 'F':
                kcal_value = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) \
                             * float(activity.replace(',', '.'))
            proteins = kcal_value * 0.3 / 4
            fats = kcal_value * 0.3 / 9
            carbs = kcal_value * 0.4 / 4

            context = {
                'form': form,
                'kcal': kcal_value,
                'prot': proteins,
                'fats': fats,
                'carbs': carbs,
            }
            return render(request, 'balanced_diet/try_service.html', context)
    else:
        form = CalorieCalcForm()
    return render(request, 'balanced_diet/try_service.html', {'form': form})

@login_required
def my_diet(request):
    return render(request, 'balanced_diet/my_diet.html')


@login_required
def new_kcal(request):
    if request.method != 'POST':
        form = User_param_form()
    else:
        form = User_param_form(data=request.POST)
        if form.is_valid():
            new_kcal = form.save(commit=False)
            new_kcal.owner = request.user
            new_kcal.save()
            return redirect('balanced_diet:my_diet')

    context = {'form': form}
    return render(request, 'balanced_diet/new_kcal.html', context)


@login_required
def edit_kcal(request):
    user = User_param.objects.get(owner=request.user)
    if request.method != 'POST':
        form = User_param_form(instance=user)
    else:
        form = User_param_form(instance=user, data=request.POST)
        if form.is_valid():
            new_kcal = form.save(commit=False)
            new_kcal.owner = request.user
            new_kcal.save()
            return redirect('balanced_diet:my_diet')
    context = {'user': user, 'form': form}
    return render(request, 'balanced_diet/edit_kcal.html', context)


@login_required
def my_diet(request):
    try:
        kcal = User_param.get_kcal(User_param.objects.get(owner=request.user))
        context = {
            'kcal': kcal[0],
            'prot': kcal[1],
            'fats': kcal[2],
            'carbs': kcal[3],
        }
        User_prefs.objects.update_or_create(
            owner=request.user,
            defaults={
                'owner':request.user,
                'kcal': kcal[0],
                'proteins': kcal[1],
                'fats': kcal[2],
                'carbs': kcal[3],
            }
        )
        return render(request, 'balanced_diet/my_diet.html', context)
    except User_param.DoesNotExist:
        return render(request, 'balanced_diet/my_diet.html')


@login_required
def progress_charts(request):
    if request.method != 'POST':
        form = User_progress_form()
    else:
        form = User_progress_form(data=request.POST)
        if form.is_valid():
            progress_charts = form.save(commit=False)
            progress_charts.owner = request.user
            progress_charts.save()
            return redirect('balanced_diet:progress_charts')

    values = User_progress.objects.filter(owner=request.user)
    context = {
        'form': form,
        'values': values
    }

    return render(request, 'balanced_diet/progress_charts.html', context)


@login_required
def input_prefs(request):
    user = User_prefs.objects.get(owner=request.user)
    if request.method != 'POST':
        form = User_prefs_form(instance=user)
    else:
        form = User_prefs_form(instance=user, data=request.POST)
        if form.is_valid():
            input_prefs = form.save(commit=False)
            input_prefs.owner = request.user
            input_prefs.save()
            return redirect('balanced_diet:my_nutrition')
    context = {'user': user, 'form': form}
    return render(request, 'balanced_diet/input_prefs.html', context)
# GET /my_nutrition/ HTTP/1.1" 200 2315
@login_required
def create_user_nutrition(request):
    try:
        user_prefs = User_prefs.get_user_prefs(User_prefs.objects.get(owner=request.user))

        dishes = Dish.objects.all()
        if user_prefs[1] == True:
            dishes = Dish.objects.exclude(recipe__product__lactose=1)
        if user_prefs[2] == True:
            dishes = dishes.exclude(recipe__product__vegan=1)
        if user_prefs[3] == True:
            dishes = dishes.exclude(recipe__product__halal=1)

        dishes_for_week = random.choices(dishes, k=21)
        weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        meals = ['BF','LN','DN']

        for weekday in weekdays:
            for meal in meals:
                    d = dishes_for_week.pop(list(dishes_for_week).index(random.choice(dishes_for_week)))
                    User_nutrition.objects.update_or_create(
                    owner= request.user,
                    weekday= weekday,
                    meal = meal,
                    defaults={
                        'owner': request.user,
                        'weekday': weekday,
                        'meal': meal,
                        'dish': d,
                        'amountofdish': user_prefs[0]/d.kcal*100
                    }
                )




        print(user_prefs)
        return render(request, 'balanced_diet/my_nutrition.html')
    except User_prefs.DoesNotExist:
        return render(request, 'balanced_diet/my_diet.html')