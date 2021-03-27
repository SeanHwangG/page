from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_progress, name='blog-home'),
    path('user', views.user, name='blog-home'),
]
