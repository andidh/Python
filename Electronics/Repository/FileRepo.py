'''
Created on Dec 7, 2015

@author: AndiD
'''

from Repository.Repository import *
from Domain.Entities import *

class ProductRepository(Repository):
    
    def __init__(self, nFN):
        Repository.__init__(self)
        self.__fileName = nFN
        self.__loadFromFile()

    def add(self, e):
        " save a product to file"
        Repository.add(self, e)
        self.__storeToFile()

    def update(self, e):
        "updates a product from the list"
        Repository.update(self, e)
        self.__storeToFile()

    def __storeToFile(self):
        f = open(self.__fileName, "w")
        prod = Repository.getAll(self)
        for p in prod:
            pf = p.get_type() + ";" + p.get_brand()+ ";" + str(p.get_quantity) + "\n"
            f.write(pf)
        f.close()

    def __loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
        except IOError as err:
            print( "ERROR: " +str(err))
        line = f.readline().strip()
        while line != " ":
            t = line.split(";")
            Repository.add(self, t)
            line = f.readline().strip()
        f.close()
