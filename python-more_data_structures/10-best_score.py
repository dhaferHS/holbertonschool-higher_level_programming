#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == None:
        return (None)
    else:
        Keymax = max(a_dictionary, key=lambda x: a_dictionary[x])
    return (Keymax)
