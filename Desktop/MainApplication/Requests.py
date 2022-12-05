import requests
import keyring
import settings
from datetime import datetime

def get(url, params=None, headers=None):
    if headers != None:
        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            if datetime.strptime(keyring.get_password('GuitarCog', 'expiration'), '%Y-%m-%dT%H:%M:%SZ') <= datetime.utcnow():
                refresh_token()
            return requests.get(url, params=params, headers=headers)
    else:
        return requests.get(url, params=params)

def post(url, json=None, files=None, headers=None):
    if headers != None:
        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            if datetime.strptime(keyring.get_password('GuitarCog', 'expiration'), '%Y-%m-%dT%H:%M:%SZ') <= datetime.utcnow():
                refresh_token()
            return requests.post(url, json=json, files=files, headers=headers)
    else:
        return requests.post(url, json=json, files=files)

def refresh_token():
    url = settings.api_path + settings.refresh_path

    response = requests.post(url, json={
        'accessToken': keyring.get_password('GuitarCog', 'token'),
        'refreshToken': keyring.get_password('GuitarCog', 'refreshToken')
    })
    if response.status_code != 200:
        keyring.delete_password('GuitarCog', 'token')
        keyring.delete_password('GuitarCog', 'refreshToken')
        keyring.delete_password('GuitarCog', 'expiration')
    else:
        response_json = response.json()
        keyring.set_password('GuitarCog', 'token', response_json['token'])
        keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
        keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])