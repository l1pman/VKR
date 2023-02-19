from django.urls import path

from . import views
app_name = 'balanced_diet'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_diet/', views.my_diet, name='my_diet'),
    path('new_kcal/', views.new_kcal, name='new_kcal'),
    path('edit_kcal/', views.edit_kcal, name='edit_kcal'),
    path('try_service/', views.try_service, name='try_service'),
    path('progress_charts/', views.progress_charts, name='progress_charts'),
    path('input_prefs/', views.input_prefs, name='input_prefs')
]