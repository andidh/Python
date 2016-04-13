'''
Created on Feb 5, 2016

@author: AndiD
'''
from repository.Srepo import SRepo
from domain.entities import Grade
from domain.entities import Student

class Grepo():
    
    def __init__(self, srepo, file):
        
        self.list = []
        self.srepo = srepo
        self.file = file
        self.__loadFromFile()
        
    def getAll(self):
        return self.list
    
    def addgrade(self, g):
        self.list.append(g)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f = open(self.file, "r")
        for line in f:
            id, object, grade = line.split(",")
            stud = self.srepo.findByID(id)
            grade = Grade(stud, object, grade)
            self.list.append(grade)
        f.close()
        
    def __storeToFile(self):
        f = open(self.file, "w")
        for g in self.list:
            line = str(g.get_stud().get_id()) + "," + g.get_object()+ "," + str(g.get_grade()) + "\n"
            f.writelines(line)
        f.close()
        
   
        
   