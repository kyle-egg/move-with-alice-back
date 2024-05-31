from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Exercise, ExerciseComment
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ExerciseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseComment
        fields = '__all__'

class PopulatedExerciseCommentSerializer(ExerciseCommentSerializer):
    owner = NestedUserSerializer()

class ExerciseSerializer(serializers.ModelSerializer):
    comments = PopulatedExerciseCommentSerializer(many=True, read_only=True)
    liked_by = NestedUserSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = '__all__'