import pickle
import os
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(emissor, receptor, missatge):
    #Buscar on es troba l'arxiu pickle (credencials)
    home_dir = os.path.expanduser ('~')
    pickle_path = os.path.join (home_dir, 'gmail.pickle')

    #Carrega les credencials que hem guardat anteriorment en un arxiu pickle
    creds = pickle.load(open(pickle_path, 'rb'))

    service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

    #Crea el missatge
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Missatge'
    msg['From'] = f'{emissor}'
    msg['To'] = f'{receptor}'
    msg.attach(MIMEText(missatge, 'plain'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw' : raw}

    message1 = body
    message = (service.users().messages().send(userId = "me", body = message1).execute()) #Envia el missatge

#Per proves de funcionament
if __name__ == "__main__":
    a = input("Escrigui la direcció des d'on s'envia el missatge: ")
    b = input ("Escrigui a on vol enviar el missatge: ")
    text = input ("Escrigui el missatge: ")
    send(a, b, text)
