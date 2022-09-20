from django.urls import path
from . import views

urlpatterns = [
    path('/', views.shop, name='shop'),
    path('/platform/<int:accountplatform_id>', views.get_platform_view, name='platform'),
    path('<int:pk>/', views.ProductView.as_view(), name='product'),
    path('/order/<int:account_id>', views.AccountOrder.as_view(), name='order'),
    path('success-order/', views.success_order, name='success'),
]
