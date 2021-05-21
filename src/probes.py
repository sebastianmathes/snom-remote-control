#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

def probe_http_auth(phone_ip, login_credentials):
    headers = {
            'User-Agent': 'Snom remote control v0.1'
    }
    url = f'http://{phone_ip}/admin'

    auth_user = login_credentials[0]
    auth_password = login_credentials[1]
    try:
        r = requests.get(url, headers=headers, 
                            auth=HTTPDigestAuth(auth_user, auth_password))
        if r.status_code == 200:
            method = "Digest"
            return method
        else:
            r = requests.get(url, headers=headers,
                                auth=HTTPBasicAuth(auth_user, auth_password))
            if r.status_code == 200:
                method = "Basic"
                return method
            else:
                return False

    except requests.exceptions.ConnectionError:
        print('Connection error, check if IP and/or port are corret.')
        return False