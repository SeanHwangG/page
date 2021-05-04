from django.shortcuts import render

from .models import File


def home(request):
  context = {'markdowns': File.objects.all()}
  return render(request, 'markdown/home.html', context)
