import asyncio

from parser.telegram import Telegram


async def main():
    # later we will put them in either config or .env
    api_id = 19115026
    api_hash = '4b1c81ce411e124c6c7d677eb7d66e9d'
    session_name = 'price_update'
    channel_link = 'https://t.me/+LmnhaSl6qqI2MTIy'

    telegram = Telegram(api_id, api_hash, session_name, channel_link)
    messages = await telegram.get_messages_today()

    print(messages)

if __name__ == '__main__':
    asyncio.run(main())

