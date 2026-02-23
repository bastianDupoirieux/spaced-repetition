import os
from dotenv import load_dotenv

from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()

def load_or_create_token_file():
    if os.path.exists(os.getenv("TOKEN_PATH")):
        return os.getenv("TOKEN_PATH")
    else:
        flow = InstalledAppFlow.from_client_secrets_file(os.getenv("CREDENTIALS_PATH"), ["https://www.googleapis.com/auth/spreadsheets"])
        credentials = flow.run_local_server(port=0)
        with open(os.getenv("TOKEN_PATH"), "w") as token:
            token.write(credentials.to_json())
        return os.getenv("TOKEN_PATH")
