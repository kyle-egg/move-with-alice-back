from django.urls import path
from .views import (
    ExerciseListView,
    ExerciseDetailView,
    ExerciseCommentListView,
    ExerciseCommentDetailView,
    ExerciseLikeView
)

urlpatterns = [
    path('', ExerciseListView.as_view()),
    path('<int:pk>/', ExerciseDetailView.as_view()),
    path('<int:exercise_pk>/comments/', ExerciseCommentListView.as_view()),
    path('<int:exercise_pk>/comments/<int:comment_pk>/', ExerciseCommentDetailView.as_view()),
    path('<int:exercise_pk>/like/', ExerciseLikeView.as_view())
]
