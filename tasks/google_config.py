
import os.path
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google_config
"""
google sheets credintioals
Email

price-updater@price-upadater.iam.gserviceaccount.com

Unique ID

118339199560342464688
 """

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '13gQBU3Q_npIco5O7iK4Ei6q1EiogqEscOl6iKG5hu9E'
SERVICE_ACCOUNT_FILE = 'credintials.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
RANGE_NAME = 'Apple ЯМ'


