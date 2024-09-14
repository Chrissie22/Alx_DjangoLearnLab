from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='post'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
