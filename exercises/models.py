from django.db import models
# from django.core.validators import MaxValueValidator

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    length = models.FloatField()
    thumbnail = models.TextField(max_length=500)
    video = models.TextField(max_length=500)
    uploaded = models.DateTimeField(auto_now_add=True, blank=True)
    types = models.ManyToManyField(
        'programs.Type',
        related_name='types'
    )
    liked_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='liked_exercises',
        blank=True
    )


    def __str__(self):
        return f'{self.name}'
    
class ExerciseComment(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    exercise = models.ForeignKey(
        Exercise,
        related_name='exercise_comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='exercise_comments_made',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.exercise} - {self.id}'

