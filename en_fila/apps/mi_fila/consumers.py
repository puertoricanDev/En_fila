import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class En_filaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['area_id']
        self.room_group_name = 'aera_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, next_position):
        text_data_json = json.loads(next_position)
        position = text_data_json['next_position']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'next_position',
                'position': position
            }
        )

    # Receive message from room group
    async def new_position(self, event):
        position = event['next_position']

        # Send message to WebSocket
        await self.send(posicion=json.dumps({
            'position': position
        }))

    
