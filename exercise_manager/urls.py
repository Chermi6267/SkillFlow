from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainings, name='trainings'),
    path('<int:workout_number>', views.certain_training, name='certain_training'),
    path('yours/', views.training_create, name='training_create'),
    path('yours/<int:workout_number>/exercises_cr', views.exercises_create, name='exercises_create'),
    path('yours/workout_del/<int:workout_id>', views.training_delete, name='training_delete'),
    path('yours/<int:workout_id>/exercise_del/<int:exercise_id>', views.exercise_delete, name='exercise_delete'),
    path('yours/<int:workout_id>/exercise_ed/<int:exercise_id>', views.exercise_edit, name='exercise_edit'), 
]