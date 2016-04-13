'''
Created on Dec 7, 2015

@author: AndiD
'''

class Product:
    
    def __init__(self, type, brand, quantity):
        self.__type = type
        self.__brand = brand
        self.__quantity = quantity
    
    def get_type(self):
        return self.__type
    
    def get_brand(self):
        return self.__brand
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, value):
        self.__quantity = ValueError
        
        
    type = property(get_type,None, None, "type's docstring")
    brand = property(get_brand, None, None, "brand's docstring")
    quantity = property (get_quantity, set_quantity, None, "quantity's docstring")
    
    
        
    def __str__(self):
        return str(self.__type) + " " + str(self.__brand) + " " + str(self.__quantity)
    
    def __repr__(self):
        return str(self)
    
    
    
def testProduct(self):
    p = Product("tablet", "samsung", 10)
    assert p.get_type() =="tablet"
    assert p.get_brand() =="samsung"
    assert p.get_quantity() == 10