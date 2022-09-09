#!/usr/bin/python3
for c in range(96, 122):
    if c % 2 == 0:
        print("{}".format(chr(c)), end="")
    else:
        print("{}".format(chr(c - 32)), end="")
