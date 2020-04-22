from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='loans-home'),
    path('about/', views.about, name='loans-about'), 
]
