# from django.urls import path
# from .views import register, user_login, user_logout, profile

# urlpatterns = [
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
#     path('profile/', profile, name='profile'),
# ]


from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
