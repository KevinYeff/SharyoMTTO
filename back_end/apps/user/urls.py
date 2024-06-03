from django.urls import path
from .views import (RegisterUserView, 
                    VerifyUserEmail, 
                    LoginUserView, 
                    PasswordResetConfirm, 
                    PasswordResetRequestView, 
                    SetNewPassword, 
                    LogoutUserView,
                    TestAuthenticationView)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify_email'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', TestAuthenticationView.as_view(), name='profile'),
    
    
    
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('set-new-password/', SetNewPassword.as_view(), name='set-new-password'),
    path('reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
