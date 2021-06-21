from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePage
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='change-password'),
    path('password_success', views.password_success, name='password-success'),
    path('<int:pk>/profile', ShowProfilePage.as_view(), name='show-profile'),
]