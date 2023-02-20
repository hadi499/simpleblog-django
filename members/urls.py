from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePassworUserView, PasswordSuccess


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', ChangePassworUserView.as_view(template_name='registration/change_password.html')),
    path('success_password/', PasswordSuccess, name='password-success')
    
]

