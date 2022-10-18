from django import views
from django.urls import path
from .views import HomeView
from .views import register
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('accounts/register', register, name='register')
]
