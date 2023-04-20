from django.contrib.auth import views as AuthViews
from django.urls import path

from .import views

urlpatterns = [
    path('',views.frontPage, name = 'frontPage'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', AuthViews.LoginView.as_view(template_name='core/login.html'), name = 'login'),
    path('logout/', AuthViews.LogoutView.as_view(), name = 'logout'),
]
