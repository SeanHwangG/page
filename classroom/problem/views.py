from rest_framework import viewsets, serializers
from rest_framework.generics import ListAPIView
from .serializers import ProblemSerializer
from django.shortcuts import render
from .models import Problem


def home(request):
  context = {'problems': Problem.objects.all()}
  return render(request, 'problem/home.html', context)


class ProblemViewSet(viewsets.ModelViewSet):
  queryset = Problem.objects.all().order_by('code')
  serializer_class = ProblemSerializer


class ProblemList(ListAPIView):
  queryset = Problem.objects.all()
  serializer_class = ProblemSerializer
