#!/usr/bin/env python3

def print_usage():
    print("Usage: Input command to send to snom phone\n\
\n\
ENTER: Send ENTER\n\
CANCEL: Send CANCEL\n\
P1-X: Send key P1-X\n\
F1-X: Send key F1-X\n\
1: Send arbitrary key command\n\
2: Send DTMF command\n\
3: Send number\n\
q: quit.")


def print_greeting():
    print('-------------------')
    print('Snom remote control')
    print('-------------------')
