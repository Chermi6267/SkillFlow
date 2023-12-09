from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/comment_chat/(?P<workout_id>\d+)/$', consumers.CommentConsumer.as_asgi()),
    re_path(r'ws/workout_chat/(?P<workout_id>\d+)/$', consumers.WorkoutConsumer.as_asgi()),
]