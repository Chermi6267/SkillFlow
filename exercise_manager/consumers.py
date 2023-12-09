import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Comment, Workout
from django.contrib.auth.models import User


# A consumer for processing comments and their likes
class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            self.workout_id = self.scope['url_route']['kwargs']['workout_id']
            self.workout_group_id = 'chatC_%s' % self.workout_id

            await self.channel_layer.group_add(
                self.workout_group_id,
                self.channel_name
            )

            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.scope["user"].is_authenticated:

            await self.channel_layer.group_discard(
                self.workout_group_id,
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        wb_type = text_data_json['type']
        if wb_type == 'create':
            await self.comment_creat(text_data_json)
        else:
            await self.comment_like(text_data_json)

# ===================================================================

    async def comment_creat(self, data):
        message = data['message']
        author = data['author']
        id = await self.save_comment(message, author, self.workout_id)
        await self.channel_layer.group_send(
            self.workout_group_id,
            {
                'type': 'comment_message',
                'message': message,
                'author': author,
                'id': id,
                'name': self.scope['user'].username
            }
        )

    async def comment_like(self, data):
        comment_id = data['comment_id']

        result = await self.is_comment_liked(data)

        await self.channel_layer.group_send(
            self.workout_group_id,
            {
                'type': 'comment_like_message',
                'comment_id': comment_id,
                'liked': result['liked'],
                'likes_count': result['likes_count'],
            }
        )

# ===================================================================

    async def comment_message(self, event):
        message = event['message']
        author = event['author']
        id = event['id']
        name = event['name']

        await self.send(text_data=json.dumps({
            'message': message,
            'author': author,
            'workout_id': self.workout_id,
            'id': id,
            'name': name,
        }))

    async def comment_like_message(self, event):
        comment_id = event['comment_id']
        liked = event['liked']
        likes_count = event['likes_count']

        await self.send(text_data=json.dumps({
            'comment_id': comment_id,
            'liked': liked,
            'likes_count': likes_count,
        }))

# ===================================================================

    @sync_to_async
    def save_comment(self, message, author, workout_id):
        user = User.objects.get(id=author)
        workout = Workout.objects.get(id=workout_id)

        return Comment.objects.create(workout=workout, author=user, text=message).id

    @sync_to_async
    def is_comment_liked(self, data):
        comment_id = data['comment_id']
        comment = Comment.objects.get(id=comment_id)
        if self.scope["user"] in comment.likes.all():
            liked = False
            comment.likes.remove(self.scope["user"])
        else:
            liked = True
            comment.likes.add(self.scope["user"])

        return {'liked': liked, 'likes_count': comment.likes.count()}

# ===================================================================


class WorkoutConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            self.workout_id = self.scope['url_route']['kwargs']['workout_id']
            self.workout_group_id = 'chatW_%s' % self.workout_id

            await self.channel_layer.group_add(
                self.workout_group_id,
                self.channel_name
            )

            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.scope["user"].is_authenticated:

            await self.channel_layer.group_discard(
                self.workout_group_id,
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        wb_type = text_data_json['type']
        if wb_type == 'like':
            await self.workout_like(text_data_json)
        else:
            await self.workout_view(text_data_json)

# ===================================================================

    async def workout_like(self, data):
        workout_id = self.scope['url_route']['kwargs']['workout_id']

        result = await self.is_workout_liked(data)

        await self.channel_layer.group_send(
            self.workout_group_id,
            {
                'type': 'workout_like_message',
                'workout_id': workout_id,
                'liked': result['liked'],
                'likes_count': result['likes_count'],
            }
        )

    async def workout_view(self, data):
        workout_id = self.scope['url_route']['kwargs']['workout_id']

        result = await self.is_workout_viewed(data)

        await self.channel_layer.group_send(
            self.workout_group_id,
            {
                'type': 'workout_view_message',
                "views_count": result['views_count']
            }
        )

# ===================================================================

    async def workout_like_message(self, event):
        workout_id = self.scope['url_route']['kwargs']['workout_id']
        liked = event['liked']
        likes_count = event['likes_count']

        await self.send(text_data=json.dumps({
            'workout_id': workout_id,
            'liked': liked,
            'likes_count': likes_count,
        }))

    async def workout_view_message(self, event):

        views_count = event['views_count']

        await self.send(text_data=json.dumps({
            'views_count': views_count,
        }))

# ===================================================================

    @sync_to_async
    def is_workout_liked(self, data):
        workout_id = self.scope['url_route']['kwargs']['workout_id']
        workout = Workout.objects.get(id=workout_id)
        if self.scope["user"] in workout.likes.all():
            liked = False
            workout.likes.remove(self.scope["user"])
        else:
            liked = True
            workout.likes.add(self.scope["user"])

        return {'liked': liked, 'likes_count': workout.likes.count()}

    @sync_to_async
    def is_workout_viewed(self, data):
        workout_id = self.scope['url_route']['kwargs']['workout_id']
        workout = Workout.objects.get(id=workout_id)
        if self.scope["user"] not in workout.number_of_views.all():
            workout.number_of_views.add(self.scope["user"])

        return {'views_count': workout.number_of_views.count()}
    
# ===================================================================
