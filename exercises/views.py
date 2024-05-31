from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Exercise, ExerciseComment
from .serializers import ExerciseSerializer, ExerciseCommentSerializer

class ExerciseListView(ListCreateAPIView):
    ''' List View for /exercises INDEX CREATE'''
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ExerciseDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /exercises/id SHOW UPDATE DELETE'''
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticated, )

class ExerciseCommentListView(APIView):
    ''' List View for /exercises/exerciseId/comments CREATE comments'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, exercise_pk):
        request.data['exercise'] = exercise_pk
        request.data['owner'] = request.user.id
        created_comment = ExerciseCommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ExerciseCommentDetailView(APIView):
    ''' DELETE COMMENT VIEW '''

    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):
        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = ExerciseComment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExerciseComment.DoesNotExist:
            raise NotFound(detail='Comment Not Found')

class ExerciseLikeView(APIView):
    ''' Adds likes to exercises or removes if already liked '''

    permission_classes = (IsAuthenticated, )

    def post(self, request, exercise_pk):
        try:
            exercise_to_like = Exercise.objects.get(pk=exercise_pk)
        except Exercise.DoesNotExist:
            raise NotFound()

        if request.user in exercise_to_like.liked_by.all():
            exercise_to_like.liked_by.remove(request.user.id)
        else:
            exercise_to_like.liked_by.add(request.user.id)

        serialized_exercise = ExerciseSerializer(exercise_to_like)

        return Response(serialized_exercise.data, status=status.HTTP_202_ACCEPTED)
