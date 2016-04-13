'''
Created on Nov 25, 2015

@author: AndiD
'''
from Domain.Entities import Client, Movie


class StoreError(Exception):
    
    def __init__(self, msg):
        self._msg = msg
        
    def __repr__(self):
        return self._msg
    

    
class ClientValidator:
    
    def __init__(self):
        pass
    
    def validcl(self, c):
        errors=[]
        if c.get_id() < 0:
            errors.append("Id must be positive")
        if c.get_name() == "":
            errors.append("Name must not be empty")
        if c.get_cnp() == "":
            errors.append("CNP must not be empty")
        if len(errors) > 0:
            raise StoreError(str(errors))
    
        
def testClValid():
    c = Client(-1,"Andi", 237288)
    v = ClientValidator()
    try:
        v.validcl(c)
        assert False
    except StoreError as ve:
        print(ve)
    

#testClValid()