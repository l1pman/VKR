# Generated by Django 4.1.6 on 2023-03-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balanced_diet', '0012_alter_user_nutrition_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_nutrition',
            name='amountofdish',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
