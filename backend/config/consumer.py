import asyncio
import json
from kafka import KafkaConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.consumer = KafkaConsumer(
            'pre_precessing',
            bootstrap_servers=['localhost:9092'],
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=False
        )
        asyncio.ensure_future(self.receive_data_from_kafka())

    async def disconnect(self, close_code):
        self.consumer.close()

    async def receive_data_from_kafka(self):
        while True:
            for message in self.consumer:
                data = message.value
                await self.send(text_data=json.dumps(data))
