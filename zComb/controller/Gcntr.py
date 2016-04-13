'''
Created on Feb 5, 2016

@author: AndiD
'''
from domain.entities import Grade
from _operator import attrgetter, itemgetter
class GradeController():
    
    def __init__(self, grepo, srepo):
        
        self.grepo = grepo
        self.srepo = srepo 
        
    def addgrade(self, sId, object, grade):
        student = self.srepo.findByID(sId)
        g = Grade(student, object, grade)
        self.grepo.addgrade(g)
        
        
    def get_all(self):
        return self.grepo.getAll()
    
    def filterGrade(self, grade):
        all = self.get_all()
        rez = []
        for g in all:
            if int(g.get_grade()) > grade:
                rez.append([g.get_stud().get_name(), str(g.get_grade()).strip()])
        rez = sorted(rez, key = itemgetter(1))
        return rez
    