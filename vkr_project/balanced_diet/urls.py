from django.urls import path

from . import views
app_name = 'balanced_diet'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_diet/', views.my_diet, name='my_diet'),
    path('new_kcal/', views.new_kcal, name='new_kcal'),
    path('edit_kcal/', views.edit_kcal, name='edit_kcal')
]