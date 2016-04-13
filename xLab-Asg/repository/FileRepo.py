'''
Created on Dec 20, 2015

@author: AndiD
'''
from repository.Repo import Repository
from domain.Entities import Student

class StudentFileRepo(Repository):

    def __init__(self, file):
        Repository.__init__(self)
        self.__file = file 
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
            s = Student(int(t[0]), t[1])
            Repository.add(self, s)
            line = f.readline().strip()
        f.close()
        
        
    def __storeToFile(self):
        f = open(self.__file, "w")
        students = Repository.getAll(self)
        for s in students:
            sf = str(s.get_id()) +  "," + s.get_name() + "\n"
            f.write(sf)
        f.close()
    
    
    
    

