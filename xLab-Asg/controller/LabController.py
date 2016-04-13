'''
Created on Dec 21, 2015

@author: AndiD
'''
from domain.Entities import *
from repository.LabFileRepo import *
from repository.FileRepo import *


class LabController:
    
    def __init__(self, repo, srepo):
        
        self.__repo = repo
        self.__srepo = srepo
        
    def createLab(self, sId, labnb, probnb):
        
        student = self.__srepo.findbyID(sId)
        lab = Lab(student, labnb, probnb)
        
        self.__repo.add(lab)
      
    def findlab(self, id):
        labs = self.__repo.getAll()
        for l in labs:
            if l.get_student().get_id() == id:
                return l
        return "Lab not found"