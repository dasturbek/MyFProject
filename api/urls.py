from django.urls import path, include
from .api import urlpatterns
from .views import post, get, put, patch, delete, detail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include(urlpatterns)),
    path('post/', post),
    path('get/', get),
    path('get/<int:pk>/', detail),
    path('put/<int:pk>/', put),
    path('patch/<int:pk>/', patch),
    path('delete/<int:pk>/', delete),    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]