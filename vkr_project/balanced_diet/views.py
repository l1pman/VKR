from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import User_param_form
from .models import User_param
# Create your views here.
def index(request):
    return render(request, 'balanced_diet/index.html')

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