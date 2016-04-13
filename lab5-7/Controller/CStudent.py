'''
Created on Nov 14, 2015

@author: AndiD
'''


from Repository.Repos import RepositoryError
from Domain.Entities import Student
from Domain.validator import ValidatorError, StoreError


class StudentController(object):
    
    def __init__(self, rep):
        self.__rep = rep
   
    def add_student(self, Id, name, group ):
        '''
        add a student
        '''
        s = Student(Id, name, group)
        try:
            self.__rep.save(s)
        except ValidatorError as ve:
            raise StoreError(ex=ve)
        except RepositoryError as re:
            raise StoreError(ex=re)

    
    def delete_student(self, Id):
        '''
        Deletes a student and its characteristics
        '''
        try:
            self.__rep.delete(Id)
        except ValidatorError as ve:
            raise StoreError(ex=ve)
        except RepositoryError as re:
            raise StoreError(ex=re)

            
                   
    def update_student(self,Id,name, group):
        '''
        Creates a new student, validates it and then replace the existing one
        '''
        student=Student(Id,name,group)
        self.__rep.update(Id, student)
 
    
    def find_student(self, Id):
        '''
        Find a student based on its Id, and returns its characteristics
        '''
        try:
            return self.__rep.find(Id)
        except ValidatorError as ve:
            raise StoreError(ex=ve)
        except RepositoryError as re:
            raise StoreError(ex=re)
            
        
    def getAllStudents(self):
        '''
        returns all the students
        '''
        return self.__rep.get_all()
    
