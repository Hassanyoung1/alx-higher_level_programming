#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence == "":
        return (0, None)
    else:
        return (str_len, sentence[0])
