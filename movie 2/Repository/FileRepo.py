'''
Created on Dec 6, 2015

@author: AndiD
'''
from Repository.Repo import *
from Domain.Entities import *

class FileMovie(Repository):
    
    def __init__(self, nameF):
        Repository.__init__(self)
        self.__namef = nameF
        self.__loadFromFile()
        
    def add(self, item):
        Repository.aadd(item)
        self.__storeToFile()
        
        
    def __storeToFile(self):
        f = open(self.__namef, "w")
        movies = Repository.get_All(self)
        for m in movies:
            mf = m.get_id() + "|" + m.get_name() + "|" + m.get_type()
            f.write(mf)
        f.close()
        
    
    
    def __loadFromFile(self):
        '''try: 
            f = open(self.__namef, "r")
        except IOError as err:
            print("Error: " + str(err))'''
        f=open(self.__namef, "r")
        line = f.readline().strip()
        while line != " ":
            t = line.split("|")
            m = Movie(t[0], t[1], t[2])
            Repository.add(self, m)
            f.readline().strip()
        f.close()
        
    
        