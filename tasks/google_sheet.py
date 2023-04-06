import os.path
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from  price_updater.parser import  telegram
from price_updater.parser.telegram import Telegram

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#Base directry of the project

SERVICE_ACCOUNT_FILE = 'D:\\TgRobot\\price_updater\\tasks\\credintials.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)

# The ID and range of a sample spreadsheet, can be changed in file google_config
SPREADSHEET_ID = '13gQBU3Q_npIco5O7iK4Ei6q1EiogqEscOl6iKG5hu9E'
RANGE_NAME = 'Apple ЯМ'


service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=RANGE_NAME).execute()

for key, value in result.items():
    print(f'{key}:{value}')
values = result.get('values', [])
print(result)












