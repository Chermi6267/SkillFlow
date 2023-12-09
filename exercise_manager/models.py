from django.db import models
from django.contrib.auth.models import User
from .utils import workout_preview_path, exercise_img_path

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    startPositionImage = models.ImageField(blank=True, upload_to=exercise_img_path, default='exercise_manager/static/img/image.svg')
    finalPositionImage = models.ImageField(blank=True, upload_to=exercise_img_path, default='exercise_manager/static/img/image.svg')

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'

    def __str__(self):
        return self.name

class Workout(models.Model):
    workoutLevels = (
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    )

    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    overview = models.TextField(blank=True)
    detailed_description = models.TextField(blank=True)
    date_of_create = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='workout_likes')
    number_of_views = models.ManyToManyField(User, blank=True, related_name='workout_views')
    preview = models.ImageField(blank=True, upload_to=workout_preview_path, default='exercise_manager/static/img/image.svg')
    level = models.CharField(max_length=1, choices=workoutLevels, default='E')

    class Meta:
        verbose_name = 'Workout'
        verbose_name_plural = 'Workout'

    def __str__(self):
        return self.name

class Comment(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')

    def __str__(self):
        return f'Comment by {self.author} on {self.workout}'