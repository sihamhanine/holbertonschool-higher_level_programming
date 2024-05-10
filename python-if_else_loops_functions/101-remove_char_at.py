#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = ""
    for i in range(len(str)):
        if i != n:
            n_str += str[i]
    return n_str
