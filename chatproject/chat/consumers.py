import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import Message, Room


class ChatConsumer(AsyncJsonWebsocketConsumer):
    groups = ['broadcast']

    async def connect(self):
        await self.accept()

        # room id を取得しインスタンス変数に格納
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        await self.channel_layer.group_add(  # グループにチャンネルを追加
            self.room_id,
            self.channel_name,
        )

    async def disconnect(self, _close_code):
        await self.channel_layer.group_discard(  # グループからチャンネルを削除
            self.room_id,
            self.channel_name,
        )

    async def receive_json(self, data):
        # メッセージをjson形式で受け取る
        message = data['message']  # 受信データからメッセージを取り出す
        user = self.scope['user'].username
        await self.createMessage(data)  # メッセージをモデルに保存する
        await self.channel_layer.group_send(  # 指定グループにメッセージを送信する
            self.room_id,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
            }
        )

    async def chat_message(self, event):
        # グループメッセージを受け取る
        message = event['message']
        user = event['user']
        # メッセージを送信する
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user': user,
        }))

    @database_sync_to_async
    def createMessage(self, event):
        room = Room.objects.get(id=self.room_id)  # room_idからRoomインスタンスを取得

        Message.objects.create(
            room=room,
            content=event['message'],
            posted_by=self.scope['user'],
        )