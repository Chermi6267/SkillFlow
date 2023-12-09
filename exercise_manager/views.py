from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import WorkoutForm, ExercisesForm
from .models import Workout, Exercise, Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth.models import User
from .decorators import coaches_only
from authentication.models import UserProfilePlus


workout_404 = 'Что-то пошло не так O_O. Проверте номер тренровки или убедитсь, что именно вы автор.'
exercise_404 = 'Что-то пошло не так O_O. Проверте номер упражнения или убедитсь, что именно вы автор.'


# Display all workouts with pagination
@login_required(login_url='login')
def trainings(request):
    # workouts = Workout.objects.all()
    workouts = Workout.objects.annotate(num_exercises=Count('exercises')).order_by('-date_of_create')

    paginator = Paginator(workouts, 64)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'trainings.html', context)


# Display certain workout
@login_required(login_url='login')
def certain_training(request, workout_number):
    workouts = Workout.objects.annotate(num_exercises=Count('exercises')).get(id=workout_number)
    exercises = workouts.exercises.all()
    comments = Comment.objects.filter(workout=workout_number).order_by('-created_at')
    author = UserProfilePlus.objects.get(user=workouts.author.id)
    is_comment_liked = {}
    for comment in comments:
        is_comment_liked[comment.id] = comment.likes.filter(id=request.user.id).exists()
        
    try:
        is_workout_liked = workouts.likes.get(id=request.user.id).id

    except User.DoesNotExist:
        is_workout_liked = False

    if is_workout_liked == request.user.id:
        is_workout_liked = True

    context = {'workout': workouts, 'exercises': exercises, 'is_workout_liked': is_workout_liked,\
               'comments': comments, 'is_comment_liked': is_comment_liked, 'author': author}
    return render(request, 'certain_training.html', context)


# Create workout
@login_required(login_url='login')
@coaches_only
def training_create(request):
    user = request.user

    form = WorkoutForm()

    workouts = Workout.objects.filter(author=user.id)

    context = {'form': form, 'workout': workouts}
    
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.author = user
            workout.save()
            return redirect('training_create')
        
    return render(request, 'training_create.html', context)


# Delete workout
@login_required(login_url='login')
@coaches_only
def training_delete(request, workout_id):
    try:
        workout = Workout.objects.get(id=workout_id, author=request.user)
        workout.exercises.all().delete()
        workout.delete()
        messages.success(request, 'Тренировка успешно удалена.')

    except Workout.DoesNotExist:
        messages.error(request, workout_404)
        return redirect('training_create')
    
    return redirect('training_create')


# Add exercise to workout
@login_required(login_url='login')
@coaches_only
def exercises_create(request, workout_number):
    try:
        workout = Workout.objects.annotate(num_exercises=Count('exercises')).get(id=workout_number, author=request.user)
        exercises = workout.exercises.all()
        form = ExercisesForm()
    except Workout.DoesNotExist:
        messages.error(request, workout_404)
        return redirect('training_create')
    
    if request.method == 'POST':
        form = ExercisesForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = Exercise.objects.create(name=request.POST['name'],
                                                description=request.POST['description'],
                                                startPositionImage=request.FILES['startPositionImage'],
                                                finalPositionImage=request.FILES['finalPositionImage']
                                                )
            workout.exercises.add(exercise)
            return redirect('exercises_create', workout_number=workout.id)
        
    context = {'workout': workout, 'exercises': exercises, 'form': form}
    return render(request, 'exercise_add.html', context)


# Delete exercise from workout
@login_required(login_url='login')
@coaches_only
def exercise_delete(request, workout_id, exercise_id):
    try:
        workout = Workout.objects.get(id=workout_id, author=request.user)

    except Workout.DoesNotExist:
        messages.error(request, workout_404)
        return redirect('training_create')
    
    if workout.author == request.user and workout.author.id == request.user.id:
        try:
            workout.exercises.get(id=exercise_id).delete()
            messages.success(request, 'Упражнение успешно удалено.')
        except Exercise.DoesNotExist:
            messages.error(request, workout_404)
            return redirect('exercises_create', workout_number=workout.id)
    else:
        messages.error(request, workout_404)
    return redirect('exercises_create', workout_number=workout.id)


# Edit exercise from training
@login_required(login_url='login')
@coaches_only
def exercise_edit(request, exercise_id, workout_id):
    try:
        workout = Workout.objects.get(id=workout_id, author=request.user)

    except Workout.DoesNotExist:
        messages.error(request, workout_404)
        return redirect('training_create')
    try:
        exercise = workout.exercises.get(id=exercise_id)

    except Exercise.DoesNotExist:
        messages.error(request, exercise_404)
        return redirect('exercises_create', workout_number=workout.id)
    
    if request.method == 'POST':
            form = ExercisesForm(request.POST, instance=exercise)
            if form.is_valid():
                form.save()
                messages.success(request, 'Данные упражнения успешно изменены.')
                return redirect('exercises_create', workout_number=workout.id)

    form = ExercisesForm(instance=exercise)
    context = {'workout': workout, 'exercise': exercise, 'form': form}
    return render(request, 'exercise_edit.html', context)