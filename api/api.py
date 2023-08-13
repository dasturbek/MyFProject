from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import PostApiViewSet, AuthorApiViewSet, post
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = DefaultRouter()

# router.register(r'post', PostApiViewSet)
router.register(r'accounts', AuthorApiViewSet)
urlpatterns += router.urls