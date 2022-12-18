import requests
import keyring
import settings
from datetime import datetime
from dateutil import parser

def get(url, params=None, needAuth=False):
    if needAuth:
        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCog', 'expiration'), ignoretz=True) <= datetime.utcnow():
                refresh_token()
            return requests.get(url, params=params, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCog', 'token')})
    else:
        return requests.get(url, params=params)

def post(url, json=None, files=None, data=None, needAuth=False):
    if needAuth:
        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCog', 'expiration'), ignoretz=True) <= datetime.utcnow():
                refresh_token()
            return requests.post(url, json=json, files=files, data=data, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCog', 'token')})
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