from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    
]
