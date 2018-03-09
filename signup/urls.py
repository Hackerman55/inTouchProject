from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.index, name = 'index'),
    path('signin/', views.index, name = 'index'),
]