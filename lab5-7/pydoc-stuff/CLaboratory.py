'''
Created on Nov 14, 2015

@author: AndiD
'''
from Repos import RepositoryError
from Entities import Laboratory
from validator import ValidatorError, StoreError


class LaboratoryController(object):
    
    def __init__(self, rep):
        self.__rep = rep
   
    def add_Laboratory(self, number, description, deadline ):
        '''
        Adds a new laboratory assignment
        '''
        l = Laboratory(number, description, deadline)
        try:
            self.__rep.save(l)
        except ValidatorError as ve:
            raise StoreError(ex=ve)
        except RepositoryError as re:
            raise StoreError(ex=re)

        
    def delete_Laboratory(self, Id):
        '''
        Deletes an assignment and its characteristics
        '''
        try:
            self.__rep.delete(Id)
        except ValidatorError as ve:
            raise StoreError(ex=ve)
        except RepositoryError as re:
            raise StoreError(ex=re)
        
        
    def find_lab(self, Nr):
        '''
        Finds an assignment by its id and returns its characteristics
        '''
        return self.__rep.find(Nr)
    
    def update_lab(self, Id, description, deadline):
        '''
        Updates an assignment
        '''
        l=Laboratory(Id, description, deadline)
        self.__rep.update(l)
        
    def getAllLabs(self):
        '''
        returns all the assignments
        '''
        return self.__rep.get_all()
