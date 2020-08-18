#!/usr/bin/env python3

import sys
from src import controls
from src import usage

if __name__ == "__main__":
    phone_ip = input("Enter phone ip: ")
    while True:
        command = input("Do something: ")
        if command != "q":
            # predefined values
            if command == "ENTER":
                controls.press_key(phone_ip,"ENTER")
            elif command == "CANCEL":
                controls.press_key(phone_ip,"CANCEL")
            elif command[0:1] == "P":
                argument = command
                controls.press_key(phone_ip,argument)
            elif command[0:1] == "F":
                argument = command
                controls.press_key(phone_ip,argument)


            # arbitrary commands
            elif command == "1":
                argument = input("Enter key command: ")
                controls.press_key(phone_ip,argument)
            elif command == "2":
                argument = input("Enter DTMF number: ")
                controls.press_key_dtmf(phone_ip,argument)
            elif command == "3":
                argument = input("Enter DTMF number: ")
                controls.press_number(phone_ip,argument)

            # help
            elif command == "h" or command == "help" or command == "?":
                usage.print_usage()
            else:
                print("No valid input, use 'help'")

        else:
            print("Exiting...")
            sys.exit(0)
