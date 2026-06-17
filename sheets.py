import gspread
from google.oauth2.service_account import Credentials

def append_to_sheet(job_title, company, status, url):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    
    # Open your tracking sheet
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/103S0QfB4EIHJr2yX9gYsE08rfCcpxcRhHOzGarUt8nw/edit?usp=sharing").sheet1
    sheet.append_row([job_title, company, status, url, "Timestamp"])