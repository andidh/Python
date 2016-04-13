'''
Created on Feb 3, 2016

@author: AndiD
'''
from Repository.Repo import BikeRepo
from Domain.Entities import Bike
from _operator import attrgetter

class File(BikeRepo):
    
    def __init__(self, file):
        BikeRepo.__init__(self)
        self.__file = file
        self.__loadFromFile()
        
    def __StoreToFile(self):
        f = open(self.__file, "w")
        bikes = BikeRepo.getAll(self)
        for b in bikes: 
            bf = str(b.get_id()) + ";" + b.get_type() + ";" + str(b.get_price()) + "\n"
            f.write(bf)
        f.close()
        
    def __loadFromFile(self):
        try: 
            f = open(self.__file, "r")
        except IOError as err:
            raise ValueError(err)
        
        line = f.readline().strip()
        while line !="":
            t = line.split(";")
            b = Bike(t[0], t[1], t[2])
            BikeRepo.add(self,b)
            line = f.readline().strip()
        f.close()
        
    def add(self, el):
        BikeRepo.add(self, el)
        self.__StoreToFile()
        
    def delete(self, id):
        BikeRepo.delete(self, id)
        self.__StoreToFile()
        
    def export(self, file):
        all = BikeRepo.getAll(self)
        all = sorted(all, key= attrgetter('price'))
        f = open(file, 'w')
        for b in all:
            bf = str(b.get_id() + "|" + b.get_type() + "|" + str(b.get_price())) + "\n"
            f.write(bf)
        f.close()
        
        
        
        