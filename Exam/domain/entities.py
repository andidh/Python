'''
Created on Feb 6, 2016

@author: AndiD
'''


class Product:
    
    def __init__(self, id, name, quantity, price):
        self._id = id
        self._name = name
        self._quantity = quantity
        self._price = price
        
    def get_id(self):
    
        return self._id
    
    def get_name(self):
        
        return self._name
    
    def get_quantity(self):
        return self._quantity
    
    def get_price(self):
        return self._price
    
    def __eq__(self, ot):
        return self.get_id() == ot.get_id() and self.get_name() == ot.get_name() and self.get_price() == ot.get_price() and self.get_quantity() == ot.get_quantity()
    
    id = property(get_id, None, None, None)
    name = property(get_name, None, None, None)
    quantity = property(get_quantity, None, None, None)
    price = property(get_price, None, None, None)
    
    def __str__(self):
        return str(self.id) + self.name + str(self.quantity) + str(self.price)
    
    
    
    
    
    
def testDomain():
    p = Product("1", "Sugar", "100", "8")
    assert p.get_id() == "1"
    assert p.get_name() == "Sugar"
    assert p.get_quantity() == "100"
    assert p.get_price() == "8"
    
testDomain()