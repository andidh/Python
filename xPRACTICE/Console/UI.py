'''
Created on Nov 26, 2015

@author: AndiD
'''
from Domain.Entities import *
from Domain.Validator import *
from Repository.Repo import *
from Controller.Controller import *

class UI:
    
    def __init__(self, ctrCl):
        self.__ctrCl = ctrCl
                
    def menu(self):
        print("0 - Exit")
        print("1 - Add client")
        print("2 - Add movie")
        
    def addClient(self):
        id = int(input("Give an id: "))
        name = input("Give a name: ")
        cnp = int(input("Give cnp: "))
        self.__ctrCl.addClient(id, name, cnp)
        print( name + " was saved")
        
    def start(self):
        while True:
            self.menu()
            cmd  = int(input("Give a command: "))
            if cmd == 0:
                break
            if cmd == 1:
                try:
                    self.addClient()
                except StoreError as ve:
                    print(ve)
                
    
    
        
        