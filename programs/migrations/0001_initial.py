# Generated by Django 5.0.6 on 2024-05-31 17:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercises', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('exercises', models.ManyToManyField(blank=True, related_name='program', to='exercises.exercise')),
                ('liked_by', models.ManyToManyField(blank=True, related_name='liked_programs', to=settings.AUTH_USER_MODEL)),
                ('type', models.ManyToManyField(blank=True, related_name='type', to='programs.type')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_comments_made', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_comments', to='programs.program')),
            ],
        ),
    ]