from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('admin-panel/', views.task_panel_admin, name='task_panel_admin'),
    path('user-panel/', views.task_panel_user, name='task_panel_user')     
]
