import asyncio

from parser.telegram import Telegram
import os
from google.oauth2 import service_account
from tasks.gsheets import   GoogleSheet

async def main():
    # later we will put them in either config or .env
    api_id = 19115026
    api_hash = '4b1c81ce411e124c6c7d677eb7d66e9d'
    session_name = 'price_update'
    channel_link = 'https://t.me/+LmnhaSl6qqI2MTIy'




    telegram = Telegram(api_id, api_hash, session_name, channel_link)
    messages = await telegram.get_messages_today()

    print(messages)

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '13gQBU3Q_npIco5O7iK4Ei6q1EiogqEscOl6iKG5hu9E'
    SERVICE_ACCOUNT_FILE = 'credintials.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    gs = GoogleSheet(SERVICE_ACCOUNT_FILE, SPREADSHEET_ID)
    gs.connect()
    #gs.print_all_data()
    gs.table_updt( messages)




if __name__ == '__main__':
    asyncio.run(main())



