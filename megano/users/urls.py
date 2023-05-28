from django.urls import path
from .views import (SignUpView, UserLogoutView, AuthView, 
                    ProfileDetail, AvatarUpdateView, PasswordUpdateView)

urlpatterns = [
    path('api/sign-up/', SignUpView.as_view(), name='sign-in'),
    path('api/sign-out/', UserLogoutView.as_view(), name='sign-out'),
    path('api/sign-in/', AuthView.as_view(), name='login'),
    path('api/profile/', ProfileDetail.as_view(), name='profile'),
    path('api/profile/avatar/', AvatarUpdateView.as_view(), name='avatar'),
    path('api/profile/password/', PasswordUpdateView.as_view(), name='password'),
    
]