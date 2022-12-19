import requests
import keyring
import settings
from datetime import datetime
from dateutil import parser

def get(url, params=None, needAuth=False):
    if needAuth:
        if keyring.get_password('GuitarCogModerator', 'token') != None and keyring.get_password('GuitarCogModerator', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCogModerator', 'expiration'), ignoretz=True) <= datetime.utcnow():
                refresh_token()
            return requests.get(url, params=params, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCogModerator', 'token')})
    else:
        return requests.get(url, params=params)

def post(url, json=None, files=None, params=None, data=None, needAuth=False):
    if needAuth:
        if keyring.get_password('GuitarCogModerator', 'token') != None and keyring.get_password('GuitarCogModerator', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCogModerator', 'expiration'), ignoretz=True) <= datetime.utcnow():
                refresh_token()
            return requests.post(url, json=json, files=files, data=data, params=params, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCogModerator', 'token')})
    else:
        return requests.post(url, json=json, files=files, data=data, params=params)

def delete(url, json=None, files=None, params=None, data=None, needAuth=False):
    if needAuth:
        if keyring.get_password('GuitarCogModerator', 'token') != None and keyring.get_password('GuitarCogModerator', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCogModerator', 'expiration'), ignoretz=True) <= datetime.utcnow():
                refresh_token()
            return requests.delete(url, json=json, files=files, data=data, params=params, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCogModerator', 'token')})
    else:
        return requests.delete(url, json=json, files=files, data=data, params=params)

def refresh_token():
    url = settings.api_path + settings.refresh_path

    response = requests.post(url, json={
        'accessToken': keyring.get_password('GuitarCogModerator', 'token'),
        'refreshToken': keyring.get_password('GuitarCogModerator', 'refreshToken')
    })
    if response.status_code != 200:
        keyring.delete_password('GuitarCogModerator', 'token')
        keyring.delete_password('GuitarCogModerator', 'refreshToken')
        keyring.delete_password('GuitarCogModerator', 'expiration')
    else:
        response_json = response.json()
        keyring.set_password('GuitarCogModerator', 'token', response_json['token'])
        keyring.set_password('GuitarCogModerator', 'refreshToken', response_json['refreshToken'])
        keyring.set_password('GuitarCogModerator', 'expiration', response_json['expiration'])