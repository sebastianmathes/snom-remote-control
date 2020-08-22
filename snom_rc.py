#!/usr/bin/env python3

import sys
from src import controls
from src import usage

if __name__ == '__main__':
    usage.print_greeting()
    phone_ip = input('Enter phone ip: ')
    wui_username = input('Enter snom WUI username: ')
    wui_password = input('Enter snom WUI password: ')
    login_credentials = [wui_username, wui_password]
    while True:
        command = input('Do something: ')
        if command != 'q':
            # predefined values
            if command == 'ENTER':
                controls.press_key(phone_ip, 'ENTER', login_credentials)
            elif command == 'CANCEL':
                controls.press_key(phone_ip, 'CANCEL', login_credentials)
            elif command[0:1] == 'P':
                argument = command
                controls.press_key(phone_ip, argument, login_credentials)
            elif command[0:1] == 'F':
                argument = command
                controls.press_key(phone_ip, argument, login_credentials)

            # arbitrary commands
            elif command == '1':
                key_argument = controls.read_argument('key')
                controls.press_key(phone_ip, key_argument, login_credentials)
            elif command == '2':
                dtmf_argument = controls.read_argument('number')
                controls.press_key_dtmf(phone_ip, dtmf_argument, login_credentials)
            elif command == '3':
                number_argument = controls.read_argument('number')
                controls.press_number(phone_ip, number_argument, login_credentials)

            # help
            elif command == 'h' or command == 'help' or command == '?':
                usage.print_usage()
            else:
                print('No valid input, use "help"')

        else:
            print('Exiting...')
            sys.exit(0)
