'''
Created on Feb 3, 2016

@author: AndiD
'''



class Console:
    
    def __init__(self, cntr):
        self.__cntr = cntr
        
    def menu(self):
        print("0 - Exit")
        print("1 - Add a bike")
        print("2 - Delete bike by type")
        print("3 - delete by price")
        print("4 - Filter by type")
        print("5 - Export bikes")
        
    def start(self):
        
        while True: 
            self.menu()
            cmd = int(input("Give a command: "))
            
            if cmd == 0:
                break
            
            if cmd == 1:
                id = int(input("Give id: "))
                type = input("Give a type: ")
                price = int(input("Give a price: "))
                self.__cntr.add(id, type, price)
            
            if cmd == 2:
                type = input("Give a type: ")
                self.__cntr.delete(type)
                
            if cmd == 3:
                price = int(input("Give a price: "))
                self.__cntr.deletePrice(price)
                
            if cmd == 4:
                type = input("Give type: ")
                all = self.__cntr.filterByType(type)
                for e in all:
                    print(e)
                    
            if cmd == 5 :
                file = input("File name: ")
                self.__cntr.export(file)