import os 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# read only access to our account data
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
CLIENT_SECRETS_FILE = 'user_secret.json'
TOKEN_FILE = 'token.json'

def get_credentials():

    creds = None
    
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # saving credentials for next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds