'''
Created on Nov 21, 2015

@author: AndiD
'''
class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group
        
    def getID(self):
        return self.__id   
    
    def getName(self):
        return self.__name 
    
    def getGroup(self):
        return self.__group
    
    def setName(self, value):
        self.__name = value
        
    def setGroup(self, value):
        self.__group = value

    
        
        
        
        
