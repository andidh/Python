'''
Created on Feb 4, 2016

@author: AndiD
'''

class UI:
    
    def __init__(self, cntr):
        self.cntr = cntr
        
    def menu(self):
        print("0 - Exit")
        print("1 - Search by name")
        print("2 - Search by group")
        print("3 - Export contacts")
        print("4 - Add contact")
        
        
    def start(self):
        
        while True:
            self.menu()
            cmd = int(input("Give a command: "))
            
            if cmd == 0:
                break;
            
            if cmd == 1:
                name = input("Give a name: ")
                self.cntr.searchName(name)
                
            if cmd == 2:
                group = input("Give a group: ")
                all = self.cntr.group(group)
                for c in all:
                    print(c)
                    
            if cmd == 3:
                file = input("Give file: ")
                self.cntr.export(file)
                
            if cmd == 4:
                try:
                    id = int(input("Give an id: "))
                    name = input("Give a name: ")
                    tel = int(input("Give a number: "))
                    group = input("Give a group: ")
                    self.cntr.add(id, name, tel, group)
                except ValueError as er:
                    print(er)
        