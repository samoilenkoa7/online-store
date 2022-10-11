from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserAccountView.as_view(), name='account'),
    path('register', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('avatar-change/', views.change_avatar, name='change')
]
