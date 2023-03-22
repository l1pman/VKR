from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class User_param(models.Model):
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    activity = models.CharField(max_length=50, choices=ACTIVITY_CHOICES, default='')

    def get_kcal(self):
        if self.gender == 'M':
            kcal_value = (10 * float(self.weight) + 6.25 * float(self.height) - 5 * float(self.age) + 5) \
                         * float(self.activity.replace(',', '.'))
        elif self.gender == 'F':
            kcal_value = (10 * float(self.weight) + 6.25 * float(self.height) - 5 * float(self.age) - 161) \
                         * float(self.activity.replace(',', '.'))
        proteins = kcal_value * 0.3 / 4
        fats = kcal_value * 0.3 / 9
        carbs = kcal_value * 0.4 / 4
        return kcal_value, proteins, fats, carbs


class User_progress(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    bust = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


class User_prefs(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lactose = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    halal = models.BooleanField(default=False)
    kcal = models.DecimalField(max_digits=6, decimal_places=2)
    proteins = models.DecimalField(max_digits=6, decimal_places=2)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)

    def get_user_prefs(self):
        lactose = self.lactose
        vegan = self.vegan
        halal = self.halal
        kcalformeal = self.kcal
        return kcalformeal, lactose, vegan, halal

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    lactose = models.BooleanField(default=False) # not lactose
    vegan = models.BooleanField(default=False) # not vegan
    halal = models.BooleanField(default=False) # not halal


class User_exclusion_products(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    kcal = models.DecimalField(max_digits=6, decimal_places=2)
    proteins = models.DecimalField(max_digits=6, decimal_places=2)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    recipetext = models.TextField(default='')


class Recipe(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amountofprod = models.CharField(max_length=50, default='')


class User_nutrition(models.Model):
    WEEKDAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    ]
    MEAL_CHOICES = [
        ('BF', 'Breakfast'),
        ('BR', 'Brunch'),
        ('LN', 'Lunch'),
        ('DN', 'Dinner')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=10, choices=WEEKDAY_CHOICES, default='')
    meal = models.CharField(max_length=10, choices=MEAL_CHOICES, default='')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    amountofdish = models.DecimalField(max_digits=6, decimal_places=2)

