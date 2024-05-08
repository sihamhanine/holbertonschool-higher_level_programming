#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{0}".format(chr(ord(c) - 32)), end="")
        else:
            print("{0}".format(c), end="")
    print()
