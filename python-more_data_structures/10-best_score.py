#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) > 0:
        Keymax = max(a_dictionary, key=lambda x: a_dictionary[x])
    return (Keymax)
    else:
        return (None)
