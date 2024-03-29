import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from news.models import News
from notifications.models import Notification


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'notifications',
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            'notifications',
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_json_data = json.loads(text_data)

        await self.save_notification(text_json_data)

        await self.channel_layer.group_send(
            'notifications', {
                'type': 'send_notification',
                'text': text_json_data.get('text'),
                'time_create': 'Только что',
            }
        )

    async def send_notification(self, event):
        await self.send(
            text_data=json.dumps({
                'text': event.get('text'),
                'time_create': event.get('time_create')
            })
        )

    @sync_to_async
    def save_notification(self, data):
        Notification.objects.create(
            text=data.get('text'),
        )