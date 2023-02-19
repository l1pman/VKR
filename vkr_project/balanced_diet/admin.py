from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User_param)
admin.site.register(User_progress)
admin.site.register(User_prefs)
admin.site.register(Dish)
admin.site.register(Product)
admin.site.register(User_exclusion_products)
admin.site.register(Recipe)