from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [path('signup/', views.signup, name="signup"),
               path('signin/', auth_views.LoginView.as_view(template_name='user/signin.html'), name='signin'),]
