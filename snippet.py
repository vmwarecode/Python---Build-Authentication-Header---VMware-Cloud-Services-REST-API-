import requests
import os 

def login():
    key = 'OAuth Refresh Token Here'
    baseurl = 'https://console.cloud.vmware.com/csp/gateway'
    uri = '/am/api/auth/api-tokens/authorize'
    headers = {'Content-Type':'application/json'}
    payload = {'refresh_token': key}
    r = requests.post(f'{baseurl}{uri}', headers = headers, params = payload)
    if r.status_code != 200:
        print(f'Unsuccessful Login Attmept. Error code {r.status_code}')
    else:
        print('Login successful. ')
        auth_json = r.json()['access_token']
        auth_Header = {'Content-Type':'application/json','csp-auth-token':auth_json}
        return auth_Header