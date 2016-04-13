'''
Created on Feb 3, 2016

@author: AndiD
'''
from Repository.Filerepo import *
from Domain.Entities import *
from _operator import itemgetter


class Controller:
    
    def __init__(self, repo):
        self.__repo = repo
        
        
    def add(self, id, type, price):
        bike = Bike(id, type, price)
        self.__repo.add(bike)
        
    def delete(self, type):
        all = self.__repo.getAll()
        for b in all:
            if b.get_type() == type:
                self.__repo.delete(b)
                continue
            
        
    def deletePrice(self, price):
        all = self.__repo.getAll()
        for b in all:
            if int(b.get_price()) > int(price):
                self.__repo.delete(b)
                continue
            
                
    def filterByType(self, type):
        all = self.__repo.getAll()
        rez = []
        for e in all:
            if e.get_type() == type:
                rez.append([e.get_id(), e.get_type(), e.get_price()])
        rez = sorted(rez, key = itemgetter(2))
        return rez
    
    def export(self, file):
        self.__repo.export(file)
    