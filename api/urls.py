from django.urls import path
from .views import *

urlpatterns = [
    path('workout/', WorkoutListCreateAPIView.as_view(),
         name='workout-list-create'),
    path('workout/<int:pk>/', WorkoutAPIView.as_view(),
         name='workout-retrieve-update-destroy'),
    path('exercise/', ExerciseListCreateAPIView.as_view(),
         name='exercise-list-create'),
    path('exercise/<int:pk>/', ExerciseAPIView.as_view(),
         name='exercise-retrieve-update-destroy'),
    path('comment/', CommentListCreateAPIView.as_view(),
         name='comment-list-create'),
    path('comment/<int:pk>/', CommentAPIView.as_view(),
         name='comment-retrieve-update-destroy'),
]
