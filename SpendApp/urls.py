from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', views.Home, name='Home'),
  path('register/', views.Register, name='Register'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('home/', views.HomePage, name='Home-page'),
  path('api/categories/', views.CategoryListView.as_view(), name='GET-ALL')
]