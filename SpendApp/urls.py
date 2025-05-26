from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.Home, name='Home'),
    path('register/', views.Register, name='Register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', views.HomePage, name='Home-page'),
    path('api/categories/', views.CategoryListView.as_view(), name='categories'),
    path('api/transactions/', views.TransactionListView.as_view(), name='transactions'),
    path('api/transactions/<int:pk>/',
         views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('api/summary/', views.TransactionSummaryView.as_view(),
         name='transaction-summary'),
    path('dashboard/', views.DashboardView, name='Dashboard'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', views.RegisterView.as_view(), name='register'),
]
