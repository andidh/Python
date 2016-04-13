'''
Created on Nov 21, 2015

@author: AndiD
'''

from Repository.repo import RepositoryStudent
from Domain.Student import Student

class StudentController:
    def __init__(self, rep):
        self.__rep = rep
        
    def addS (self, id, name, group):
        s = Student(id, name, group)
        self.__rep.addStudent(s)
        return s
        