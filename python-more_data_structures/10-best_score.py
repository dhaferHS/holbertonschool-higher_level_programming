#!/usr/bin/python3
def best_score(a_dictionary):
    Keymax = max(a_dictionary, key= lambda x: a_dictionary[x])
    return(Keymax)
