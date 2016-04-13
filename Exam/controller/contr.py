'''
Created on Feb 5, 2016

@author: AndiD
'''
from domain.entities import Product
from _operator import itemgetter

class Controller:
    
    def __init__(self, repo, val):
        
        self._repo = repo
        self._val = val
        self.cart = []
        self.cartValue = 0
        self.income = 0
        self.product = []
    
    def add(self, id, name, quantity, price):
        '''
        This function creates an object of type Product and adds it to the inventory
        input:
            id - integer
            name - string
            quantity - integer 
            price - integer
        '''
        
        prod = Product(id, name, quantity, price)
        self._val.validate(prod)
        self._repo.add(prod)
        
      
    def update(self, id, quantity, price):
        self._repo.update(id, quantity, price)
        
    
    def addCart(self, id, quantity):
        '''
        This function adds the desired product to the cart
        input:
            id of the product
            quantity desired
        '''
        all = self._repo.getAll()
        for p in all:
            if p.get_id() == id:
                if quantity > p.get_quantity():
                    raise ValueError("Quantity not available")
                else:
                    p.get_quantity = p.get_quantity() - quantity
                    self.cart.append([p.get_id(), p.get_name(), quantity, (p.get_price())*(quantity)])
                    self.cartValue += (p.get_price())*(quantity)

    def showCart(self):
        '''
        This function displays the items from the cart
        '''
        return self.cart
    
    def finalize(self, ans):
        '''
        This function finalizes the purchase
        If the answer is Yes(Y) then the cart is emptied and the price of the items is added to the income
        '''
        if ans == "Y":
            self.income = self.cartValue
            self.product.extend(self.cart)
            self.cart.clear()
        if ans == "N":
            self.cart.clear()
            
    def getIncome(self):
        '''
        This function returns the total income
        '''
        return self.income
    
    def report(self):
        all = self.product
        all = sorted(all, key = itemgetter(3), reverse = True)
        return all
    
            