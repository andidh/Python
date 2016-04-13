'''
Created on Dec 7, 2015

@author: AndiD
'''
from Domain.Entities import *
from Utility.utils import *



class ProductRepository:
    
    def __init__(self, nameF):
        self.__nameF = nameF
        
    def save(self, product):
        """
        save product 
        """
        allP=self.__loadAllFromFile()
        for p in allP:
            if p.get_type()==product.get_type() and p.get_brand()==product.get_brand():
                raise ValueError("Product already exists")
        fH = open(self.__nameF,"a")
        self.__writeToFile(product, fH)
        fH.close()
        
    def __writeToFile(self,product,fh):
        """
        writes in file the product
        """
        fh.write(product.get_type() + "," + product.get_brand() + "," + str(product.get_quantity()))
        fh.write("/n")
        
    def __loadAllFromFile(self):
        """
        loads all the products from file
        """
        fH=openFileCreateIfNeeded(self.__nameF)
        rez=[]
        with fH:
            for line in fH:
                attrs=line.split(",")
                if len(attrs)!=3:
                    continue
                rez.append(Product(attrs[0],attrs[1],int(attrs[2])))
        return rez
    
    def get_AllProducts(self):
        """
        returns a list with all the products
        """
        return self.__loadAllFromFile()
    
    def __saveAll(self,allP):
        """
        saves all the products in file 
        Rewrites it
        """
        fH = open(self.__numeFis, "w")
        for p in allP:
            self.__writeToFile(p, fH)            
        fH.close()
    
    
    
    def update(self, type, brand, product):
        '''
        Updates the quanityt of a given product
        returns the brand and the new quantity
        '''
        allP=self.__loadAllFromFile()
        for p in range(len(allP)):
            if allP[p].get_type()==type and allP[p].get_brand()==brand:
                if product.get_quantity()> allP[p].get_quantity():
                    raise ValueError("There are not enough products of the given type and brand")
                else:
                    product.get_quantity=allP[p].get_quantity()-product.get_quantity()
                    allP[p]=product
                    self.__saveAll(allP)
                    return


