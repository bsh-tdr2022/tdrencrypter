import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow


# Specify permissions to send and read/write messages
# Find more information at:
# https://developers.google.com/gmail/api/auth/scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.modify']



home_dir = os.path.expanduser('~')


json_path = os.path.join(home_dir, 'Desktop', 'TDR', 'Credencials', 'credentials.json')


flow = InstalledAppFlow.from_client_secrets_file(json_path, SCOPES)


creds = flow.run_local_server(port=0)


pickle_path = os.path.join(home_dir, 'gmail.pickle')
with open(pickle_path, 'wb') as token:
    pickle.dump(creds, token)