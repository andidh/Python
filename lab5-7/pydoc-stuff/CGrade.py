'''
Created on Nov 14, 2015

@author: AndiD
'''
from _operator import attrgetter

from Repos import RepositoryError
from DTO import sumDTO
from Entities import Grade, Student
from validator import ValidatorError, StoreError


class GradeController():
    def __init__(self, repoG, repoS, repoL):
        self.__repoG=repoG
        self.__repoS=repoS
        self.__repoL=repoL
        
    def associate(self, Id, number, Grade):
        '''
        Assigns to every student a laboratory
        Input - id (integer)
              - number (integer) - the number of laboratory
              - grade (float) - the grade for the assignment
        '''
        try: 
            stud=self.__repoS.find(Id)
            lab=self.__repoL.find(number)
            n=Grade(stud, lab, Grade)
            self.__repoG.save(n)
        except ValidatorError as ve:
            raise StoreError(ex=ve)
        except RepositoryError as re:
            raise StoreError(ex=re)
        return n

    def getDTO(self):
        '''
        returns the grades
        '''
        return self.__repoG.getAllDTO()
    
    def Sort(self):
        '''
        sorts the list by name
        '''
        allDTO=self.getDTO()
        allDTO=sorted(allDTO, key=attrgetter('name','Grade'),reverse=False)
        return allDTO


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
                rez.append(name)
        return rez
    
    
    def avrg(self):
        list=[]
        all=self.getDTO()
        rez=self.namelist()
        for s in rez:
            sum=0
            cont=0
            for n in all:
                if s==n.get_name():
                    cont=cont+1
                    sum=sum+int(n.get_grade())
            sum=sum/cont
            stud=[s,sum]
            if sum<5:
                list.append(stud)
        return list
    
    
