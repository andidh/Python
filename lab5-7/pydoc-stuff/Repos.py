'''
Created on Nov 14, 2015

@author: AndiD
'''


from validator import StoreError
from DTO import sumDTO 

class RepositoryError(StoreError):
    pass

class DuplicateID(RepositoryError):
    pass

class SLRepo(object):
    def __init__(self, validator):
        self.__items = {}
        self.__validator = validator

    def saveS(self, item):
        '''Saves a student ''' 
        
        if item.Id in self.__items:
            raise DuplicateID("Student is already added")
        self.__validator.validateS(item)
        self.__items[item.Id] = item
        
    def saveL(self, item):
        '''
        Save a assignment
        '''
        if item.Id in self.__items:
            raise DuplicateID("Assignment is already added")
        self.__validator.validateL(item)
        self.__items[item.Id] = item

        
    def size(self):
        '''
        Return the number of assignments/students
        '''
        return len(self.__items)
    
    def delete(self, item_Id):
        '''
        deletes a student/assignment
        '''
        if not item_Id in self.__items:
            raise RepositoryError("Id is already added")
        del self.__items[item_Id]

        
    def find(self, item_Id):
        '''
        find a student/assignment based on Id and returns its characteristics
        '''
        
        if not item_Id in self.__items:
            raise RepositoryError("Id does not exist")
        return self.__items[item_Id]
        
    
    def update(self, item_Id, new):
        '''
        updates a student / assignment and returns its new characteristics
        '''
        if not item_Id in self.__items:
            raise RepositoryError("Id does not exist")
        
        self.__items[item_Id]= new
        return self.__items[item_Id]
    
    
    def get_all(self):
        '''
        returns all the students/assignments
        '''
        if len(self.__items)==0:
            return("-")
        return list(self.__items.values())

    

class GradeRepo(object):
    
    def __init__(self, validator):
        self.__grade=[]

        
    def find(self, student, lab, grade):
        for n in self.__grade:
            if n.get_stud()==student and n.get_lab()==lab and n.get_grade()==grade:
                return n
        return None
    
    def save(self, n):
        '''
        save a grade
        '''
        if n in self.__grade:
            raise ValueError("Grade already exists")
        else:
            self.__grade.append(n)
            
    
    
    def getAllDTO(self):
        '''
        Returns the list of objects student-assignment-grade
        '''
        rez=[]
        
        for n in self.__note:
            s=sumDTO(n.get_stud().get_name(),n.get_lab().get_description(),n.get_grade())
            rez.append(s)
        return rez
    


        
