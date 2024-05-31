from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Program, Type, ProgramComment
from .serializers import ProgramSerializer, TypeSerializer, ProgramCommentSerializer

class ProgramListView(ListCreateAPIView):
    ''' List View for /programs INDEX CREATE'''
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ProgramDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /program/id SHOW UPDATE DELETE'''
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsAuthenticated, )

class TypeListView(ListCreateAPIView):
    ''' List View for /types INDEX CREATE'''
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ProgramCommentListView(APIView):
    ''' List View for /programs/programId/comments CREATE comments'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, program_pk):
        request.data['program'] = program_pk
        request.data['owner'] = request.user.id
        created_comment = ProgramCommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ProgramCommentDetailView(APIView):
    ''' DELETE COMMENT VIEW '''

    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):
        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = ProgramComment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProgramComment.DoesNotExist:
            raise NotFound(detail='Comment Not Found')

class ProgramLikeView(APIView):
    ''' Adds likes to programs or removes if already liked '''

    permission_classes = (IsAuthenticated, )

    def post(self, request, program_pk):
        try:
            program_to_like = Program.objects.get(pk=program_pk)
        except Program.DoesNotExist:
            raise NotFound()

        if request.user in program_to_like.liked_by.all():
            program_to_like.liked_by.remove(request.user.id)
        else:
            program_to_like.liked_by.add(request.user.id)

        serialized_program = ProgramSerializer(program_to_like)

        return Response(serialized_program.data, status=status.HTTP_202_ACCEPTED)