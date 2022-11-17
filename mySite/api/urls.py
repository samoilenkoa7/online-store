from django.urls import path
from api import views


urlpatterns = [
    path('accounts/list/', views.AccountListAPIView.as_view(), name='accounts_list'),
]