from django import forms
from .models import User_param, User_progress, User_prefs
from django.contrib.auth.models import User


class User_param_form(forms.ModelForm):
    class Meta:
        model = User_param
        fields = ['gender','weight','height','age','activity']
        labels = {
            'gender': 'Пол',
            'weight': 'Вес',
            'height': 'Рост',
            'age':'Возраст',
            'activity': 'Активность'
        }
class User_progress_form(forms.ModelForm):
    class Meta:
        model = User_progress
        fields = ['weight','bust','waist','hips']
        labels = {
            'weight':'Вес',
            'bust':'Обхват груди',
            'waist':'Обхват талии',
            'hips':'Обхват бедер'
        }

class CalorieCalcForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]
    ACTIVITY_CHOICES = [
        ('1,2', 'Сидячий образ жизни.'),
        ('1,375', 'До трех малоинтенсивных тренировок в неделю.'),
        ('1,55', 'Тренировки три-четыре раза в неделю, тренировки интенсивные, но не тяжелые.'),
        ('1,7',
         'Ежедневные занятия спортом или ежедневная работа, связанная с большим количеством перемещений и ручного труда.'),
        ('1,9', 'Экстремальная активность. Профессиональный спортсмен или работа с тяжестями и т.д.')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Пол')
    weight = forms.IntegerField(label='Вес')
    height = forms.IntegerField(label='Рост')
    age = forms.IntegerField(label='Возраст')
    activity = forms.ChoiceField(choices=ACTIVITY_CHOICES, label='Активность')


class User_prefs_form(forms.ModelForm):
    class Meta:
        model = User_prefs
        fields = ['lactose', 'vegan', 'halal']
        labels = {
            'lactose': 'У меня непереносимость лактозы',
            'vegan': 'Я веган',
            'halal': 'Я мусульманин'
        }
