'''
Created on Dec 21, 2015

@author: AndiD
'''

from repository.Repo import *
from domain.Entities import *

class LabRepo(Repository):
    
    def __init__(self, file, srepo):
        Repository.__init__(self)
        self.__file = file 
        
        self._srepo = srepo
        
        self.__loadFromFile()
        
        
    def add(self, e):
        Repository.add(self, e)
        self.__storeToFile()
        
    def __loadFromFile(self):
        try:
            f = open(self.__file, "r")
        except IOError as e:
             print("IOError " + str(e))
        line = f.readline().strip()
        while line != "":
            t = line.split(",")
            
            stud = self._srepo.findbyID(int(t[0]))
                                           
            l = Lab(stud, t[1], t[2])
            Repository.add(self, l)
            line = f.readline().strip()
        f.close()
    
    def __storeToFile(self):
        f = open(self.__file, "w")
        labs = Repository.getAll(self)
        for l in labs:
            lf = str(l.get_student().get_id()) + "," + str(l.get_id()) + "," + str(l.get_problemnb()) + "\n"
            f.write(lf)
        f.close()
    
   
 