from django.shortcuts import render


def home(request):
  return render(request, 'classroom/home.html')
