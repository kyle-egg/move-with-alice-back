from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Program, Type, ProgramComment
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ProgramCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramComment
        fields = '__all__'

class PopulatedProgramCommentSerializer(ProgramCommentSerializer):
    owner = NestedUserSerializer()

class ProgramSerializer(serializers.ModelSerializer):
    comments = PopulatedProgramCommentSerializer(many=True, read_only=True)
    liked_by = NestedUserSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'