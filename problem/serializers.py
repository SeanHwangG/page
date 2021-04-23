from rest_framework import serializers

from problem.models import Problem


class ProblemListSerializer(serializers.ListSerializer):
  def create(self, validated_data):
    books = [Book(**item) for item in validated_data]
    return Book.objects.bulk_create(books)


class ProblemSerializer(serializers.ModelSerializer):
  list_serializer_class = ProblemListSerializer

  class Meta:
    model = Problem
    fields = '__all__'

  def to_representation(self, instance):
    data = super().to_representation(instance)
