'''
Created on Dec 7, 2015

@author: AndiD
'''
from Domain.Entities import Product
from operator import attrgetter

class ProductController:
    
    def __init__(self,repo):
        self.__repo=repo
    
            
    def sort(self):
        allProducts=self.__repo.getAll()
        allProducts=sorted(allProducts, key=attrgetter('quantity'),reverse=True)
        return allProducts

    def update_product(self,type, brand, quantity):
        
       
        product=Product(type, brand,quantity)
        self.__repo.update(product)

    def getAll(self):
        return self.__repo.getAll()


