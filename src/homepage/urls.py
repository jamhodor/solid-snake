from django.urls import path, include
from homepage import views

urlpatterns = [
    path('', views.home, name='home'),
]