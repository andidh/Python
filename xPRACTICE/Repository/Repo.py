'''
Created on Nov 25, 2015

@author: AndiD
'''
from Domain.Validator import *
from Domain.Entities import Client, Movie


class ClientRepo():
    
    def __init__(self):
        self.__clients = {}
        
    def store(self, c):
        if c.get_id() in self.__clients:
            raise StoreError("Id is already in use")
        self.__clients[c.get_id()] = c
        
    def size(self):
        return len(self.__clients)
        
    


def testAddClient():
    rep = ClientRepo()
    c = Client(1, "Andi", 23213)
    rep.store(c)
    assert rep.size() == 1
    

testAddClient()        