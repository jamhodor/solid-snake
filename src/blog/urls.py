from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]