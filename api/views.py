# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.shortcuts import get_object_or_404, redirect
# from exercise_manager.models import Workout, Comment
# from exercise_manager.forms import CommentForm
# from django.contrib.humanize.templatetags.humanize import naturaltime


# class WorkoutLikeAPIToggle(APIView):
#     authentication_classes = (authentication.SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request, workout_id=None):
#         obj = get_object_or_404(Workout, id=int(request.POST['workout_id']))
#         user = self.request.user
#         updated = False
#         liked = False

#         if user.is_authenticated:
#             if user in obj.likes.all():
#                 liked = False
#                 obj.likes.remove(user)
#             else:
#                 liked = True
#                 obj.likes.add(user)
#             updated = True

#         data = {
#             "updated_likes_count": obj.likes.count(),
#             "updated": updated,
#             "liked": liked,
#         }

#         return Response(data)

#     def get(self, request, workout_id=None):
#         return redirect('trainings')


# class WorkoutViewsAPI(APIView):
#     authentication_classes = (authentication.SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request, workout_id=None):
#         obj = get_object_or_404(Workout, id=int(request.POST['workout_id']))
#         user = self.request.user
#         viewed = False

#         if user.is_authenticated:
#             if user in obj.number_of_views.all():
#                 viewed = True
#             else:
#                 obj.number_of_views.add(user)


#         data = {
#             "number_of_views": obj.number_of_views.count(),
#             "viewed" : viewed,
#         }

#         return Response(data)

#     def get(self, request, workout_id=None):
#         return redirect('trainings')


# class CommentAPI(APIView):
#     authentication_classes = (authentication.SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
#         if request.method == 'POST':
#             if request.POST['type'] == "create":
#                 workout = get_object_or_404(Workout, id=int(request.POST['workout_id']))
#                 form = CommentForm({'text': request.POST['comment']})

#                 if form.is_valid():
#                     comment = form.save(commit=False)
#                     comment.author = request.user
#                     comment.workout = workout
#                     comment.save()

#                 data = {'comment_id': comment.id,
#                         'comment_text': comment.text,
#                         'comment_author':comment.author.username,
#                         'comment_time': naturaltime(comment.created_at),
#                         'likes_count': comment.likes.count()
#                         }

#             else:
#                 obj = get_object_or_404(Comment, id=int(request.POST['comment_id']))
#                 user = self.request.user
#                 updated = False
#                 liked = False

#                 if user.is_authenticated:
#                     if user in obj.likes.all():
#                         liked = False
#                         obj.likes.remove(user)
#                     else:
#                         liked = True
#                         obj.likes.add(user)
#                     updated = True

#                 data = {
#                     "updated_likes_count": obj.likes.count(),
#                     "updated": updated,
#                     "liked": liked,
#                 }

#         return JsonResponse(data)

#     def get(self, request):
#         return redirect('trainings')
from rest_framework import generics
from .serializers import *
from exercise_manager.models import *


class WorkoutAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutListCreateAPIView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ExerciseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class CommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
