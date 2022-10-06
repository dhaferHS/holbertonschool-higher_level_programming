#!/usr/bin/python3
"""base class"""

class Base:
    _nb_objects = 0

    def __init__(self, id=None):
        """id"""
    
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
