#!/usr/bin/env python3

import requests

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


def press_key(phone_ip, key_value):
    url = f'http://{phone_ip}/command.htm?key={key_value}'
    send_key(url)


def press_key_dtmf(phone_ip, key_dtmf_value):
    url = f'http://{phone_ip}/command.htm?key_dtmf={key_dtmf_value}'
    send_key(url)


def press_number(phone_ip, number_value):
    url = f'http://{phone_ip}/command.htm?number={number_value}'
    send_key(url)


def send_key(url):
    try:
        r = requests.get(url, headers=headers)
        return r.status_code
    except requests.exceptions.ConnectionError:
        print("Connection error, check if IP and/or port are corret.")
        return False


def read_argument(mode):
    while True:
        argument = input("Which command? ")
        if mode == "key":
            if argument in commands:
                return argument
            elif argument == "list" or argument == "l":
                list_commands()
            else:
                print("Invalid command, try again or use l/list for help")

        elif mode == "number":
            return argument

        else:
            print("Invalid mode, please check.")
            return False


def list_commands():
    for command in commands:
        print(command)
