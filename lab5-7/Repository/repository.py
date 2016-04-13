'''
Created on Nov 2, 2015

@author: AndiD
'''
from Domain.Entities import  Student, Laboratory, Grade
from Domain.DTO import sumDTO



class StudentRepo:
    def __init__(self):
        self._students = []
        
    def storeS(self, s):
        for i in range(len(self._students)):
            if self._students[i].get_id() == s.get_id():
                raise ValueError("Id already exists")
        return self._students.append(s)
    
        
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
          for i in range(len(self._students)):
            if self._students[i].get_id()==s.get_id():
                self._students[i] = s
                return
            raise ValueError("Student does not exist")
    
    def get_all(self):
        s=[]
        for i in range(len(self._students)):
            s.append(self._students[i])
        return s
        for m in range(len(s)):
            return s[m]
    
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
            if p.get_number()==prb:
                return p
        return None
    
    def removelab(self,prb):
        p=self.findbyprb(prb)
        if p == None:
            raise ValueError("Lab does not exist")
        self._lab.remove(p)
        
    def updateprb(self, prb):

        for i in range(len(self._lab)):
            if self._lab[i].get_id()==prb.get_id():
                self.__lab[i] = prb
                return
        raise ValueError("Lab does not exist")

class GradeRepo:
    
    def __init__(self):
        self._grade=[]
        
    def findby(self,s,p,grade):
        for n in self._grade:
            if n.get_stud()==s and n.get_lab()==p and n.get_grade()==grade:
                return n
        return None
    
    def save(self,n):
        if n in self._grade:
            raise ValueError("Grade exists")
        self._grade.append(n)
        
    def getAllDTO(self):
        rez=[]
        for s in self._grade:
            rez.append(sumDTO(s.get_stud().get_name(), s.get_lab().get_number(),s.get_grade()))
        return rez
        
