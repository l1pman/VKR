from django.urls import path

from . import views
app_name = 'balanced_diet'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_diet/', views.my_diet, name='my_diet'),
]