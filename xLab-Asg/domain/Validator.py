'''
Created on Dec 20, 2015

@author: AndiD
'''
from domain.Entities import Student

class CustomException(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        
    def getMessage(self):
        return self.msg
    
    def __str__(self):
        return self.msg
    
    
class StudentValidator:
    
    def validate(self, stud):
        errors = []
        if stud.get_id() < 0 or stud.get__id() == "":
            errors.append("Id must not be empty or <0")
        if stud.get_name() == "":
            errors.append("Name must not be empty")
        if len(errors)>0:
            raise CustomException(str(errors))
            
    
    
    
    
    
 