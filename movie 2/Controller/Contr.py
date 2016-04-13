'''
Created on Dec 5, 2015

@author: AndiD
'''


from Domain.Entities import Movie
from Domain.Validator import *
from Repository.Repo import *


class MovieController():
    
    def __init__(self, val, rep):
        self.__val = val
        self.__rep = rep
        
    def create(self, id, name, type):
        m = Movie(id, name, type)
        self.__val.validate(m)
        self.__rep.add(m)
        
    