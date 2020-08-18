#!/usr/bin/env python3

import requests

headers = {
        'User-Agent': 'Snom remote control v0.1'
}

def press_key(phone_ip, key_value):
    url = f'http://{phone_ip}/command.htm?key={key_value}'
    try:
        r = requests.get(url, headers=headers)
        return r.status_code
    except requests.exceptions.ConnectionError:
        print("Connection error, check if IP and/or port are corret.")
        return False

def press_key_dtmf(phone_ip, key_dtmf_value):
    url = f'http://{phone_ip}/command.htm?key_dtmf={key_dtmf_value}'
    try:
        r = requests.get(url, headers=headers)
        return r.status_code
    except requests.exceptions.ConnectionError:
        print("Connection error, check if IP and/or port are corret.")
        return False

def press_number(phone_ip, number_value):
    url = f'http://{phone_ip}/command.htm?number={number_value}'
    try:
        r = requests.get(url, headers=headers)
        return r.status_code
    except requests.exceptions.ConnectionError:
        print("Connection error, check if IP and/or port are corret.")
        return False