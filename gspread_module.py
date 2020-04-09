import gspread
from oauth2client.service_account import ServiceAccountCredentials

def setup_gs():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    clients= gspread.authorize(creds)

    sheet = clients.open("employee_db").sheet1

    return sheet                                                                #This will return a sheet object, which will be used to access the sheet



