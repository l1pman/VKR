from django.contrib import admin
from .models import *
# Register your models here.
class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'lactose', 'vegan', 'halal')
admin.site.register(User_param)
admin.site.register(User_progress)
admin.site.register(User_prefs)
admin.site.register(Dish)
admin.site.register(Product, AdminProducts)
admin.site.register(User_exclusion_products)
admin.site.register(Recipe)