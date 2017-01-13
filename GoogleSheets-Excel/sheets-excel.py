

from __future__ import print_function
import httplib2
import os
import xlwt
from datetime import datetime
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import time

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    #PreReqs: install xlwt.   pip install xlwt
    #Preqs: install google library pip install --upgrade google-api-python-client

    #Replace the below array with the  ID of the Spreadsheets needed to be populated
    ArrayOfSpreadSheets=['1n_iN5iVKVb8sdQh4GxuEB76m60qMpE1qQ74cDDg2HQ0','1CeopiL7T-OCOoAO_g4KWKcFXTc7ktbfyEkq2iV6OHqo']

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    #Replace the Ranges of the Spreadsheets you want in the array below. Consider the title of the cells for each sheet. 
    #Do not include the cells with the titles of the cells in the rangename EXCEPT for the first sheet.  
    rangeName=['A1:C3','A2:C2']
    #Creates the book 
    book = xlwt.Workbook(encoding="utf-8")
    #Create's a Sheet. Change name to desired value
    sheet1 = book.add_sheet("Sheet 1")
    currentspreadsheet=0
    NumRows=0
    while(currentspreadsheet!=len(ArrayOfSpreadSheets)):
        spreadsheetId = ArrayOfSpreadSheets[currentspreadsheet]
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName[currentspreadsheet]).execute()
        values = result.get('values', [])
    #NumRows represents the number of rows    
        #NumColumns represents teh number of columns. CHANGE THIS TO THE NUMBER OF COLUMNS IN YOUR SPREADSHEET. 
        #The number of columns should be equal in both sheets 
        NumColumns=3    
        if not values:
            print('No data found.')
        else:
            for row in values:            
                i=0
                while(i<NumColumns):
                    sheet1.write(NumRows,i,row[i])
                    i+=1
                NumRows+=1
            
        currentspreadsheet+=1
    #CHANGE THE NAME OF THE EXCEL SPREADSHEET TO YOUR LIKING    
    book.save('example.xlsx')            
  
if __name__ == '__main__':
    main()