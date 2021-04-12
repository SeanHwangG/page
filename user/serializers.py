from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["user_id"]

  def create(self, validated_data):
    return User.objects.create(validated_data)

  def update(self, instance, validated_data):
    User.objects.create(validated_data)
    instance.save()
    return instance

  def to_representation(self, instance):
    data = super().to_representation(instance)
