from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)
from . import apis

# api modelviewset setting 
app_name = "auth"


urlpatterns = [
    path("api-v1/auth-login", apis.AdminLoginAPI.as_view(), name="auth-login"),    
    path("api-v1/auth/register", apis.AdminRegisterAPI.as_view(), name="auth-register"),
    
    # token
    path("token", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]