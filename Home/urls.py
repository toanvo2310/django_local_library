from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Index),
    #path('Blog/', views.Blog),
    path('Contact/', views.Contact, name='Contact'),
    path('Register/', views.register, name='Register'),
    path('Login/', auth_views.LoginView.as_view(template_name = 'Pages/Login.html'), name='Login'),
    path('Logout/', auth_views.LogoutView.as_view(next_page = '/'), name = 'Logout'),
]
