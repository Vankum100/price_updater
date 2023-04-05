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



    def remove_special_c(self,text):
        fixed =""
        for i in text:
            if i.isalnum() or i.isspace():
                fixed +=i

        return fixed


    def update_table(self,sheet_file_name,telegram_data):
        self.sheet = self.client.open_by_key(self.sheet_file_ID).worksheet('Sony YM')
        #updating logic to be here

        product_name = []
        product_price = []
        for i in telegram_data:
            for k in i:
                product_name.append(k)
                product_price.append(i[k])

        prices_column_index = self.sheet.find('Цена опт., р').col

        _names_column_values = self.sheet.col_values(2)

     #   try:

        for i in range (len(product_name)):
              if _names_column_values[i-1] == product_name[i-1]:
                  print(self.sheet.cell(i,product_price[i]))
                  self.sheet.update_cell(i,prices_column_index,product_price[i])
                  print(self.sheet.cell(i,product_price[i]))
       # except Exception as e :
       #     print(f'\n{e}\n')




    def _update_table(self, sheet_file_name, telegram_data):
        self.sheet = self.client.open_by_key(self.sheet_file_ID).worksheet('Sony YM')
        # updating logic to be here
        prices_column_index = self.sheet.find('Цена опт., р').col
        selling_column_index = 7
        _names_column_values = self.sheet.col_values(2)
        for item in telegram_data:
            for name in item :
                cell = self.sheet.find(name)
                if name == cell:
                    print(self.sheet.cell(cell.row, prices_column_index.col))
                    self.sheet.update_cell(cell.row, prices_column_index, item[name])
                    self.sheet.updaate_cell(cell.row,selling_column_index,(item[name]*1.1))
                    print(self.sheet.cell(cell.row, prices_column_index.col))






    def print_all_data(self):
        for row in self.sheet.get_all_values():
            print(row)












