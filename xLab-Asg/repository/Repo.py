'''
Created on Dec 20, 2015

@author: AndiD
'''
from domain.Validator import *

class Repository:
    
    def __init__(self):
        self.__list = []
        
    def add(self, s):
        if self.findbyID(s.get_id()) != None:
            raise CustomException("Id already exists")
        self.__list.append(s)
        
    def findbyID(self, id):
        for el in self.__list:
            if str(el.get_id()) == str(id):
                return el
        return None
            
    
    def getAll(self):
        return self.__list
    
    def __len__(self):
        return len(self.__list)
        
    
    def __str__(self):
        r = "Elements from Repository:\n"
        for e in self.__list:
            r += str(e)
            r += "\n"
        return r