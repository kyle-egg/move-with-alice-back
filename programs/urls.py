from django.urls import path
from .views import (
    ProgramListView,
    TypeListView,
    ProgramDetailView,
    ProgramCommentListView,
    ProgramCommentDetailView,
    ProgramLikeView
)

urlpatterns = [
    path('', ProgramListView.as_view()),
    path('types/', TypeListView.as_view()),
    path('<int:pk>/', ProgramDetailView.as_view()),
    path('<int:program_pk>/comments/', ProgramCommentListView.as_view()),
    path('<int:program_pk>/comments/<int:comment_pk>/', ProgramCommentDetailView.as_view()),
    path('<int:program_pk>/like/', ProgramLikeView.as_view())
]
