'''
Created on Feb 3, 2016

@author: AndiD
'''

from Domain.Entities import Bike

class BikeRepo():
    
    def __init__(self):
        
        self.list = []
        
    def add(self, item):
        self.list.append(item)
        
    def findByID(self, id):
        for el in self.list:
            if str(el.get_id()) == str(id):
                return el
        return None
    
    def getAll(self):
        return self.list
    
    def delete(self, elem):
        self.list.remove(elem)
        
        
        