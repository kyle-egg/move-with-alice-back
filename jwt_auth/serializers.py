from exercises.serializers import ExerciseSerializer, ExerciseCommentSerializer
from programs.serializers import ProgramSerializer, ProgramCommentSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
# import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})

        # try:
        #     validation.validate_password(password=password)
        # except ValidationError as err:
        #     raise ValidationError({'password': err.messages})

        data['password'] = make_password(password)

        return data


    class Meta:
        model = User
        fields ='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    liked_programs = ProgramSerializer(many=True)
    program_comments_made = ProgramCommentSerializer(many=True)
    liked_exercises = ExerciseSerializer(many=True)
    exercise_comments_made = ExerciseCommentSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'dob', 'liked_programs', 'program_comments_made', 'liked_exercises', 'exercise_comments_made')
