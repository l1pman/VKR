from django import forms
from .models import User_param
from django.contrib.auth.models import User


class User_param_form(forms.ModelForm):
    class Meta:
        model = User_param
        fields = ['gender','weight','height','age','activity','lactose','vegan']


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
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    weight = forms.IntegerField()
    height = forms.IntegerField()
    age = forms.IntegerField()
    activity = forms.ChoiceField(choices=ACTIVITY_CHOICES)

