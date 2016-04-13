'''
Created on Dec 5, 2015

@author: AndiD
'''
from Domain.Entities import Movie
from Domain.Validator import StoreError

class Repository:
    
    def __init__(self):
        self.__list = []
        
    def add(self, item):
        '''if self.find(item.get_id()) != None:
            raise StoreError("Id already added")'''
        self.__list.append(item)
        
        
    def find(self, itemID):
        for e in self.__list:
            if str(e.get_id()) == str(itemID):
                return e
        return None
    
    def get_All(self):
        return self.__list