from django.urls import path
from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns=[path("",api_home),
path("auth/",obtain_auth_token),
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]