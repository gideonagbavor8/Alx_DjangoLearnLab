from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

from .views import UserProfileView

urlpatterns += [
    path('profile/', UserProfileView.as_view(), name='profile'),
]
