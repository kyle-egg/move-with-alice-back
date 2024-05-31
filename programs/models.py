from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Program(models.Model):
    name = models.CharField(max_length=200)
    exercises = models.ManyToManyField(
        'exercises.Exercise',
        related_name='program',
        blank=True
    )
    type = models.ManyToManyField(
        Type,
        related_name='type',
        blank=True
    )
    uploaded = models.DateTimeField(auto_now_add=True, blank=True)
    liked_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='liked_programs',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'
    
class ProgramComment(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(
        Program,
        related_name='program_comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='program_comments_made',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.program} - {self.id}'
