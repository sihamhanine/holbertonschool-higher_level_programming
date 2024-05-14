#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if sentence == "":
            fchar = None
            lent = 0
            return (0, None)
        else:
            fchar = sentence[0]
            lent = len(sentence)
            return (lent, fchar)
