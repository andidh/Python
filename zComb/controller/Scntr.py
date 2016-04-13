'''
Created on Feb 5, 2016

@author: AndiD
'''
from repository.Srepo import SRepo
from domain.entities import Student

class SController:
    
    def __init__(self, srepo):
        self.srepo = srepo
        
        
    def add(self, id, name, group):
        s = Student(id, name, group)
        self.srepo.add(s)
        
    def get_all(self):
        return self.srepo.getAll()
    
    def delete(self, id):
        self.srepo.delete(id)