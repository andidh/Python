'''
Created on Dec 5, 2015

@author: AndiD
'''
from Domain.Validator import *


class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    def menu(self):
        print("0 - exit")
        print("1 - add a movie")
        print("2 - update")
        
    def start(self):
        while True:
            self.menu()
            cmd = int(input("Give a command: "))
            
            if cmd == 0:
                break
            
            if cmd == 1:
                id = int(input("Give an id: "))
                name = input("Give a name: ")
                type = input("Give a type: ")
                try:
                    self.__ctrl.create(id, name, type)
                except StoreError as ve:
                    print(ve)
                
                