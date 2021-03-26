from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserSerializer
from .models import User
from .models import User


def home(request):
  context = User.objects.all()
  return render(request, "user/home.html")


class UserList(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserCreate(CreateAPIView):
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)
