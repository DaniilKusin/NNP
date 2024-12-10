from django.urls import path
from .views import get_registration_page, CustomLoginView, register
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg_page/', get_registration_page, name='reg_page'),
    path('register/', register, name='register'),
    path('login/', views.get_authorization_page(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/profile/', views.get_profile_page, name='profile')
]