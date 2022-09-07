from django.urls import path
from . import views


urlpatterns = [
    path('/', views.shop, name='shop'),
    path('<int:pk>/', views.ProductView.as_view(), name='product'),
    path('<int:pk>/order', views.OrderAccount.as_view(), name='order'),
    path('success-order/', views.success_order, name='success'),
]
