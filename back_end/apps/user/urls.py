from django.urls import path
from .views import RegisterUserView, VerifyUserEmail, LoginUserView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify_email'),
    path('login/', LoginUserView.as_view(), name='login'),
    # path('token/', views.CreateTokenView.as_view()),
    # path('user/', views.RetrieveUpdateUserView.as_view()),
]
