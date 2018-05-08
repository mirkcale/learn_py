#!/usr/bin/env python3
class Field:
    def __init__(self, name, cloumn_type):
        self.name = name
        self.cloumn_type = cloumn_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)