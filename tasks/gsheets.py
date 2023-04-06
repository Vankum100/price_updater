import os.path
import re

import gspread
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from  price_updater.parser import  telegram
from price_updater.parser.telegram import Telegram



class GoogleSheet:
    def __init__(self,credential_file_path, sheet_file_ID):
        self.credential_file_path = credential_file_path
        self.sheet_file_ID = sheet_file_ID
        self.client = None
        self.sheet = None
        self.connect()


    def connect(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        credentials =  service_account.Credentials.from_service_account_file(self.credential_file_path, scopes = self.scopes)
        self.client = gspread.authorize(credentials)
        self.sheet = self.client.open_by_key(self.sheet_file_ID).worksheet('Sony YM')



    def remove_special_charachters(self,text):
        fixed =""
        for i in text:
            if i.isalnum() or i.isspace():
                fixed +=i

        return fixed



    def _update_table(self,  telegram_data):
        #//take a list of worksheets names[Sony YM,Yandex YM...] as a list
        # ,iterate it ,to apply the logic for all sheets

        self.sheet = self.client.open_by_key(self.sheet_file_ID).worksheet('Sony YM')
        # updating logic to be here
        prices_column_index = self.sheet.find('Цена опт., р').col
        selling_column_index = 7
        _names_column_values = self.sheet.col_values(2)
        for item in telegram_data:
            for name in item :
                cell = self.sheet.find(name)
                if cell is not None and name == cell.value:
                    if name == cell.value:
                        print(self.sheet.cell(cell.row, prices_column_index).value)
                        self.sheet.update_cell(cell.row, prices_column_index, item[name])
                        self.sheet.update_cell(cell.row,selling_column_index,float(item[name])*1.1)
                        print(self.sheet.cell(cell.row, prices_column_index).value)



    #this code is the same as above but optimized
    #to reduce the api call requests,we extract the data all at once using get_bath()
    def table_updt(self,telegram_data):
        self.sheet = self.client.open_by_key(self.sheet_file_ID).worksheet('Sony YM')
        prices_column_index = self.sheet.find('Цена опт., р').col
        selling_column_index = 7
        _names_column_values = self.sheet.col_values(2)
        data_range = self.sheet.range(1, 1, self.sheet.row_count, len(_names_column_values))
        data = {}
        for cell in data_range:
            data[(cell.row, cell.col)] = cell.value
        for item in telegram_data:
            for name in item:
                for row, col in data:
                    if data[(row, 2)] == name:
                        if data[(row, 2)] == name:
                            print(data[(row, prices_column_index)])
                            self.sheet.update_cell(row, prices_column_index, item[name])
                            self.sheet.update_cell(row, selling_column_index, float(item[name]) * 1.1)
                            print(data[(row, prices_column_index)])
                            break



    def print_all_data(self):
        for row in self.sheet.get_all_values():
            print(row)












