'''
Created on Nov 2, 2015

@author: AndiD
'''
from Domain.Entities import  Student, Laboratory, Grade



class StudentRepo:
    def __init__(self):
        self._students = []
        
    def storeS(self, s):
        if s in self._students:
            raise ValueError("Id exists")
        self._students.append(s)
    
        
    def RemoveS(self, id):
        s=self.findbyID(id)
        if s==None:
            raise ValueError("The student does not exist")
        self._students.remove(s)
    
    def findbyID(self, id):
        for s in self._students:
            if s.get_id() == id:
                return s
        return None
    
    def UpdateS(self, s):
          for i in range(len(self.__students)):
            if self._students[i].get_id()==s.get_id():
                self.__students[i] = s
                return
            raise ValueError("Student does not exist")
    
    def get_all(self):
        return self._students
    
class LabRepo:
    
    def __init__(self):
        self._lab=[]
        
    def storeL(self,p):
        if p in self._lab:
            raise ValueError("Laboratory already exists")
        self._lab.append(p)
        
    def get_all(self):
        return self._lab
    
    def findbyprb(self,prb):
        for p in self._lab:
            if p.get_numar()==prb:
                return p
        return None
    
    def removelab(self,prb):
        p=self.findbyprb(prb)
        if p == None:
            raise ValueError("Problem does not exist")
        self._lab.remove(p)
        
    def updateprb(self, prb):

        for i in range(len(self._lab)):
            if self._lab[i].get_id()==prb.get_id():
                self.__lab[i] = prb
                return
        raise ValueError("laboratorul nu exista")

class GradeRepo:
    
    def __init__(self):
        self.grade=[]
        
    def findby(self,s,p,grade):
        for n in self._grade:
            if n.get_stud()==s and n.get_lab()==p and n.get_grade()==grade:
                return n
        return None
    
    def save(self,n):
        if n in self._grade:
            raise ValueError("Grade exists")
        self._grade.append(n)
        
