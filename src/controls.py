#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

headers = {
        'User-Agent': 'Snom remote control v0.1'
}

commands = ['OFFHOOK',
            'ONHOOK',
            'RIGHT',
            'LEFT',
            'UP',
            'DOWN',
            'VOLUME_UP',
            'VOLUME_DOWN',
            'MENU',
            'REDIAL',
            'DND',
            'REC',
            'SPEAKER',
            'HEADSET',
            'TRANSFER',
            'F_HOLD',
            '0','1','2','3','4','5','6','7','8','9']


def press_key(phone_ip, key_value, login_credentials):
    url = f'http://{phone_ip}/command.htm?key={key_value}'
    send_key(url, login_credentials)


def press_key_dtmf(phone_ip, key_dtmf_value, login_credentials):
    url = f'http://{phone_ip}/command.htm?key_dtmf={key_dtmf_value}'
    send_key(url, login_credentials)


def press_number(phone_ip, number_value, login_credentials):
    url = f'http://{phone_ip}/command.htm?number={number_value}'
    send_key(url, login_credentials)


def send_key(url, login_credentials):
    try:
        auth_user = login_credentials[0]
        auth_password = login_credentials[1]
        r = requests.get(url, headers=headers,
                         auth=HTTPDigestAuth(auth_user, auth_password))
        #print(r.status_code)
        if r.status_code != 200:
            print(f'Got response {r.status_code}, please check.')

        return r.status_code
    except requests.exceptions.ConnectionError:
        print('Connection error, check if IP and/or port are corret.')
        return False


def read_argument(mode):
    while True:
        if mode == 'key':
            argument = input('Which command? ')
            if argument in commands:
                return argument
            elif argument == 'list' or argument == 'l':
                print('Here is a list of available commands:\n', commands)
                #list_commands()
            else:
                print('Invalid command, try again or use l/list for help')

        elif mode == 'number':
            argument = input('Which number? ')
            return argument

        else:
            print('Invalid mode, please check.')
            return False


def list_commands():
    for command in commands:
        print(command)
