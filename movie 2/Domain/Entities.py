'''
Created on Dec 5, 2015

@author: AndiD
'''

class Movie:
    def __init__(self, id, name, type):
        self.__id = id
        self.__name = name
        self.__type = type
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def set_name(self, val):
        self.__name = val
    
    def set_type(self, val):
        self.__type = val
    
    def __repr__(self):
        return str(self.__id) + " " + self.__name + " " + self.__type
    
    '''def __eq__(self, other):
        if self.__id == other.get_id():
            return True'''