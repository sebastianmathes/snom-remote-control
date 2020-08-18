#!/usr/bin/env python3

import sys
from src import controls
from src import usage

if __name__ == "__main__":
    b = input("Gief ip: ")
    while True:
        a = input("Do something: ")
        if a != "q":
            # predefined values
            if a == "ENTER":
                controls.press_key(b,"ENTER")
            elif a == "CANCEL":
                controls.press_key(b,"CANCEL")

            # arbitrary commands
            elif a == "1":
                c = input("Enter key command: ")
                controls.press_key(b,c)
            elif a == "2":
                c = input("Enter DTMF number: ")
                controls.press_key_dtmf(b,c)
            elif a == "3":
                c = input("Enter DTMF number: ")
                controls.press_number(b,c)

            # help
            elif a == "h" or a == "help" or a == "?":
                usage.print_usage()
            else:
                print("No valid input, use 'help'")

        else:
            print("cu")
            sys.exit(0)
