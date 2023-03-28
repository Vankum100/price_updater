from datetime import datetime

from telethon import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputChannelEmpty


class Telegram:
    def __init__(self, api_id, api_hash, session_name, channel_link):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_name = session_name
        self.channel_link = channel_link
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)

    async def get_messages_today(self):
        await self.client.start()
        channel = await self.get_channel_entity(self.channel_link)
        if isinstance(channel, InputChannelEmpty):
            print("The specified channel does not exist.")
            await self.client.disconnect()
            return {}
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
        products = []
        async for message in self.client.iter_messages(channel):
            if message.date.replace(tzinfo=None) > today:
                lines = message.text.strip().split('\n')

                for line in lines:
                    # Split the line into parts
                    parts = line.strip().split()

                    if len(parts) > 0 and parts[-1].isnumeric():
                        # product_data = {'product': ' '.join(parts[0:-1]), 'price': parts[-1]}
                        product_data = {' '.join(parts[0:-1]): parts[-1]}
                        products.append(product_data)
                    # else:
                    #     print('parts ', parts)
                    #     continue
        await self.client.disconnect()
        return products

    async def get_channel_entity(self, channel_link):
        try:
            result = await self.client(GetFullChannelRequest(channel=channel_link))
        except ValueError:
            result = InputChannelEmpty()
        return result.chats[0]
