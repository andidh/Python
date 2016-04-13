'''
Created on Dec 7, 2015

@author: AndiD
'''
class UI:
    def __init__(self,ProductController):
        self.__pcontroller= ProductController
    
    def meniu(self):
        print("0 - Exit")
        print("1 - Sort by type")
        print("2 - Update Quantity")
    
    def start_ui(self):    
        while True:
            self.meniu()
            cmd=int(input("Give command: "))
                
            if cmd==0:
                break
 
            if cmd==1:
                allP=self.__pcontroller.sort()
                for p in allP:
                    print(p)
                    
            if cmd==2:
                type = input("Give type: ")
                brand = input("Give brand: ")
                quantity = int(input("Give new quantity:"))
                try:
                    self.__pcontroller.update_product(type, brand,quantity)
                    allP=self.__pcontroller.getAll()
                    for p in allP:
                        print(p)
                except ValueError as msg:
                    print(msg)