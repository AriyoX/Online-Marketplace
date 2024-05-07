from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<int:pk>', views.categorical, name='categorical'),
    path('contact/',views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.user_logout, name='logout'),
]