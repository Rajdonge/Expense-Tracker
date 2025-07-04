from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    ExpenseIncomeListView,
    ExpenseIncomeDetailView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    
    path('expenses/', ExpenseIncomeListView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseIncomeDetailView.as_view(), name='expense-detail'),
]