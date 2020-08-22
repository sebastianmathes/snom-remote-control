#!/usr/bin/env python3

import sys
from src import controls
from src import usage

if __name__ == '__main__':
    usage.print_greeting()
    phone_ip = input('Enter phone ip: ')
    while True:
        command = input('Do something: ')
        if command != 'q':
            # predefined values
            if command == 'ENTER':
                controls.press_key(phone_ip, 'ENTER')
            elif command == 'CANCEL':
                controls.press_key(phone_ip, 'CANCEL')
            elif command[0:1] == 'P':
                argument = command
                controls.press_key(phone_ip, argument)
            elif command[0:1] == 'F':
                argument = command
                controls.press_key(phone_ip, argument)

            # arbitrary commands
            elif command == '1':
                key_argument = controls.read_argument('key')
                print(key_argument)
                controls.press_key(phone_ip, key_argument)
            elif command == '2':
                dtmf_argument = controls.read_argument('number')
                controls.press_key_dtmf(phone_ip, dtmf_argument)
            elif command == '3':
                number_argument = controls.read_argument('number')
                print('Number is: ', number_argument)
                controls.press_number(phone_ip, number_argument)

            # help
            elif command == 'h' or command == 'help' or command == '?':
                usage.print_usage()
            else:
                print('No valid input, use "help"')

        else:
            print('Exiting...')
            sys.exit(0)
