from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from .models import User, Membership
from problem.models import Problem, Tag, Solution
from django.http import HttpResponse, JsonResponse


def user(request):
  context = User.objects.get(name="황규승")
  return render(request, "user/home.html", {"user": context.__dict__})


def user_list(request):
  if request.method == "GET":
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(dir(serializer))
    print((serializer))
    return JsonResponse(serializer.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    serialzer = UserSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


class UserCreate(CreateAPIView):
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)
