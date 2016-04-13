'''
Created on Dec 20, 2015

@author: AndiD
'''


class Student: 
    
    def __init__(self, id, name):
        self.__id = id
        self.__name = name 
        
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, val):
        self.__name = val
        
    
    id = property(get_id, None, None, None)
    name = property(get_name, set_name, None, None)
    
    def __str__(self):
        return str(self.id) + " " + self.name
    
class Lab:
    
    def __init__(self, student, labnb, problemnb):
        self.__student = student
        self.__labnb = labnb
        self.__problemnb = problemnb
        
    def get_student(self):
        return self.__student
    
    def get_id(self):
        return self.__labnb
    
    def get_problemnb(self):
        return self.__problemnb
    
    def set_labnb(self, val):
        self.__labnb = val
        
    def set_problemnb(self, val):
        self.__problemnb = val
    
    student = property(get_student, None, None, None)
    numberlab = property(get_id, set_labnb, None, None)
    numberprb = property(get_problemnb, set_problemnb, None)
    
    def __str__(self):
        return str(self.student) + " " + str(self.numberlab) + " " + self.numberprb    
        
    