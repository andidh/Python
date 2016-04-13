'''
Created on Feb 6, 2016

@author: AndiD
'''

from domain.entities import Product

class Validator:
    
    def validate(self, p):
        err = []
        if p.get_name() == "":
            err.append("Name cannot be empty")
        if int(p.get_quantity()) < 0:
            err.append("Quantity cannot be negative")
        if int(p.get_price()) < 0:
            err.append("Price cannot be negative")
        
        if len(err) > 0:
            raise ValueError(err)
        
        
def testValidator():
    v = Validator()
    p = Product("1", "sugar", "-100", "9")
    try:
        v.validate(p)
        return False
    except ValueError as err:
        print(err)
        
#testValidator()