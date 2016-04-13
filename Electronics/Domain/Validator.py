'''
Created on Dec 7, 2015

@author: AndiD
'''

class ValidatorProduct:
    def valideaza(self,product):
        errors=[]
        if product.get_type=="":
            errors.append("Type cannot be empty")
        if product.get_brand=="":
            errors.append("Brand cannot be empty")
        if product.get_quantity<0:
            errors.append("Quantity cannot be < 0")
        if len(errors)>0:
            raise ValueError(errors)
