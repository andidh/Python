'''
Created on Dec 21, 2015

@author: AndiD
'''
from domain.Validator import *
from domain.Entities import Student

class StudentController:
    
    def __init__(self, repo, valid):
        self.__repo = repo
        self._valid = valid
        
    def add(self, id, name):
        stud = Student(id, name)
        self.__repo.add(stud)
        
        
    def getAll(self):
        return self.__repo.getAll()
    
    def find(self, studid):
        return self.__repo.findbyID(studid)