'''
Created on Feb 6, 2016

@author: AndiD
'''
from domain.entities import Product

class Repository:
    
    def __init__(self, file):
        
        self.list = []
        self._file = file 
        
        self.__loadFromFile()
        
        
    def add(self, prod): 
        '''
        Function which adds a product to the file
        prod = object of type Product
        ''' 
        for p in self.list:
            if str(p.get_id()) == str(prod.get_id()):
                print("Id already exists")
        self.list.append(prod)
        self.__storeToFile(prod)
    
    def update(self, id, quantity, price):
        el = self.find(id)
        if el == None:
            raise ValueError("Element not found!")
        el.get_quantity = el.get_quantity() + quantity
        el.get_price = el.get_price() + price
        self.__storeToFile()
    
   
    def find(self, id):
        for p in self.list:
            if str(p.get_id()) == str(id):
                return p
        return None
    """
    def add(self, prod): 
        '''
        Function which adds a product to the file
        prod = object of type Product
        ''' 
        for p in self.list:
            if str(p.get_id()) == str(prod.get_id()):
                print("Id already exists")
                p.get_quantity = p.get_quantity() + prod.get_quantity
                p.get_price = p.get_price() + prod.get_price()
            else:
                self.list.append(prod)
                self.__storeToFile()
        """
        
    def getAll(self):
        return self.list
    
    def __loadFromFile(self):
        '''
        Function which loads the products from the file 
        output : file.txt
        
        '''
        f = open(self._file, "r")
        for line in f:
            id, name, quantity, price = line.split(",")
            p = Product(id, name, quantity, price)
            self.list.append(p)
        f.close()
            
    def __storeToFile(self, p):
        '''
        Function which stores the products to the file
        '''
        f = open(self._file, "a")
        line = str(p.get_id()) + "," + p.get_name() + "," + str(p.get_quantity()) + "," + str(p.get_price())+ "\n"
        f.writelines(line)
        f.close()
        
    def __len__(self):
        return len(self.list)
    
    
