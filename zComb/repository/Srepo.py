'''
Created on Feb 5, 2016

@author: AndiD
'''
from domain.entities import Student


class SRepo:
    
    def __init__(self, file):
        self.list = []
        self.file = file
        self.__loadFromFile()
        
        
    def add(self, s):
        self.list.append(s)
        self.__storeToFile()
        
        
    def getAll(self):
        return self.list
    
    
    def delete(self, id):
        stud = self.findByID(id)
        self.list.remove(stud)
        self.__storeToFile()
        
    
    def findByID(self, id):
        for s in self.list:
            if str(s.get_id()) == str(id):
                return s
    
    def __loadFromFile(self):
        f = open(self.file, "r")
        for line in f:
            id, name, group = line.split(",")
            s = Student(id, name, group)
            self.list.append(s)
        f.close()
        
    def __storeToFile(self):
        f = open(self.file, "w")
        for s in self.list:
            line = str(s.get_id()) + "," + s.get_name() + "," + str(s.get_group()) + "\n"
            f.writelines(line)
        f.close()
            
            