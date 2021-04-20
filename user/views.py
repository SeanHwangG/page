from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import JSONParser
from django.contrib import messages
from problem.models import Problem, Tag, Solution
from django.http import HttpResponse, JsonResponse
from .forms import UserRegistrationForm
from .serializers import UserSerializer
from .models import User, Membership


def register(request):
  if request.method == "POST":
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"Account created for {username}")
      return redirect('classroom-home')
  else:
    form = UserRegistrationForm()
  return render(request, 'user/register.html', {'form': form})


def user(request):
  context = User.objects.get(name="황규승")
  return render(request, "user/home.html", {"user": context.__dict__, 'form': form})


def user_list(request):
  if request.method == "GET":
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
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
