'''
Created on Nov 2, 2015

@author: AndiD
'''

from Repository.repository import StudentRepo, LabRepo, GradeRepo
from Domain.Entities import Student, Laboratory, Grade


        
class SController:
    def __init__(self,rep):
        self._rep=rep
    
    def add(self, id, name, group):
        s=Student(id,name, group)
        self._rep.storeS(s)
        return s
    
    def deletestud(self,id):
        self._rep.RemoveS(id)
        
    def findstud(self,id):
        return self._rep.findbyID(id)
    
    def upstud(self, id, name, group):
        s = Student(id, name, group)
        self._rep.UpdateS(s)
        return s
    
    def allstud(self):
        return self._rep.get_all()
    

class LController :
    
    def __init__(self,rep):
        self._rep=rep
        
    def add(self,nb,description,deadline):
        p=Laboratory(nb,description,deadline)
        self._rep.storeL(p)
        return p
    
    def deletelab(self,nb):
        self._rep.removelab(nb)
        
    def findlab(self,nb):
         return self._rep.findbyprb(nb)
     
    def updatelab(self, name, description, deadline):
        p = Laboratory(name, description, deadline)
        self._rep.updateprb(p)
        return p
    
    def alllab(self):
        return self._rep.get_all()

class GController:
    
    def __init__(self,repog,repos,repol):
        self._repog=repog
        self._repos=repos
        self._repol=repol
        
    def associate(self,id,nb,grade):
        s=self._repos.findbyID(id)
        p=self._repol.findbyprb(nb)
        n=Grade(s,p,grade)
        self._repog.save(n)
        return n
    
    def getDTO(self):
        return self._repog.getAllDTO()

    
    def namelist(self):
        all=self.getDTO()
        rez=[]
        for s in all:
            name=s.get_name()
            currentname=None
            for n in rez:
                if n==name:
                    currentname=n
            if currentname==None:
                rez.append(n)
        return rez
    
    def avrg(self):
        list=[]
        all=self.getDTO()
        rez=self.namelist()()
        for s in rez:
            sum=0
            cont=0
            for n in all:
                if s==n.get_name():
                    cont=cont+1
                    sum=sum+n.get_grade()
            sum=sum/cont
            stud=[s,sum]
            if sum<5:
                list.append(stud)
        return list
            
  