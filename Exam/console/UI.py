'''
Created on Feb 5, 2016

@author: AndiD
'''


class UI:
    
    def __init__(self, contr):
        
        self._contr = contr 
        
        
    def menu(self):
        print("0 - Exit")
        print("1 - Add product")
        print("2 - Add to cart")
        print("3 - Finalize")
        print("4 - Show income")
        print("5 - Update product")
        print("6 - Report")
        
    def start(self):
        
        while True:
            
            self.menu()
            cmd = int(input("Give a command: "))
            
            if cmd == 0:
                break
            
            if cmd == 1:
                id = int(input("Give id: "))
                name = input("Give name: ")
                quantity = int(input("Give quantity: "))
                price = int(input("Give price: "))
                try: 
                    self._contr.add(id, name, quantity, price)
                    print("Product was successfully added")
                except ValueError as err:
                    print(err)
                    
            if cmd == 2:
                id = int(input("Give id :"))
                quantity = int(input("Give quantity: "))
                try:
                    self._contr.addCart(id, quantity)
                    print("Product added to cart")
                except ValueError as err:
                    print(err)
                    
            if cmd == 3:
                all = self._contr.showCart()
                for p in all:
                    print(p)
                ans = input("Want to finalize? Y/N ")
                self._contr.finalize(ans)
                
            if cmd == 4:
                income = self._contr.getIncome()
                print("Total income: ", income)
                
            if cmd == 5:
                id = int(input("Id of the product: "))
                quantity = int(input("Give quantity: "))
                price = int(input("Give price: "))
                self._contr.update(id, quantity, price)
                
            if cmd == 6:
                all = self._contr.report()
                for p in all:
                    print(p)
                