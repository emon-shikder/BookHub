from django.urls import path, include
from account.views import (
    UserSignUpPageView,
    UserLoginPageView,
    UserLogoutView,
    ProfilePageView,
)

urlpatterns = [
    path("sign-up/", UserSignUpPageView.as_view(), name="signup"),
    path("login/", UserLoginPageView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<str:profilenav>/", ProfilePageView, name="profile"),
]
