'''
Created on Dec 5, 2015

@author: AndiD
'''
from Domain.Entities import Movie


class StoreError(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
    
class ValidatorMovie:
    
    def validate(self, item):
        errors = []
        if item.get_id() < 0:
            errors.append("Id cannot be less than 0")
        if item.get_name() == "":
            errors.append("Name cannot be emtpy")
        if item.get_type() == "":
            errors.append("Type cannot be empty")
        if len(errors) > 0:
            raise StoreError(str(errors))
        
def testValidate():
    val = ValidatorMovie()
    c = Movie(-1, "DKNY", "Type")
    try:
        val.validate(c)
        return False
    except StoreError as ve:
        print(ve)

    