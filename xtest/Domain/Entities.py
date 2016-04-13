'''
Created on Feb 3, 2016

@author: AndiD
'''


class Bike:
    
    def __init__(self, id, type, price):
        
        self.__id = id
        self.__type = type
        self.__price = price
        
    def get_id(self):
        return self.__id
    
    def get_type(self):
        return self.__type
    
    def get_price(self):
        return self.__price
    
    def __eq__(self, other):
        return self.get_id() == other.get_id() and self.get_type() == other.get_type and self.get_price() == other.get_price()
    
    id = property(get_id, None, None, None)
    type = property(get_type, None, None, None)
    price = property(get_price, None, None, None)
    
    def __str__(self):
        return str(self.id) + " " + self.type + " " + str(self.price)
    
    
def testBike():
    b = Bike("100" , "mountain" , "500")
    assert b.get_id() == "100"
    assert b.get_type() == "mountain"
    assert b.get_price() == "500"
    
testBike()
        