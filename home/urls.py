from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ProfilView, UserView, regView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView, name='post_view'),
    path('profile/', ProfilView.as_view(), name='profil'),
    path('user/<int:pk>/', UserView.as_view(), name='user_view'),
    path('new-post/', PostCreateView.as_view(), name='post_create_view'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit_view'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete_view'),
    path('reg_user/', regView, name='sign_up_view'),
]