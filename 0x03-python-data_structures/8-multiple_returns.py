#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence == "":
        return (0, 0)
    else:
        return (str_len, sentence[0])
