'''
Created on Feb 5, 2016

@author: AndiD
'''
from builtins import object


class Student: 
    
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_group(self):
        return self.__group
    
    def __eq__(self, ot):
        return self.get_id() == ot.get_id() and self.get_name() == ot.get_name() and self.get_group() == ot.get_group()
    
    id = property(get_id, None, None, None)
    name = property(get_name, None, None, None)
    group = property(get_group, None, None, None)
    
    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.group)
    
    
class Grade:
    
    def __init__(self, student, object, grade):
        self.__student = student
        self.__object = object
        self.__grade = grade
        
    def get_stud(self):
        return self.__student
    
    def get_object(self):
        return self.__object
    
    def get_grade(self):
        return self.__grade
    
    student = property(get_stud, None, None, None)
    object = property(get_object, None, None, None)
    grade = property(get_grade, None, None, None)
    
    def __str__(self):
        return str(self.student) +" " + self.object + " " + str(self.grade)