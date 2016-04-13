'''
Created on Dec 21, 2015

@author: AndiD
'''
from domain.Validator import CustomException
from domain.Entities import *
from repository.FileRepo import *
from repository.Repo import *
from repository.LabFileRepo import *
from controller.LabController import *
from controller.StudentController import *

class UI:
    
    def __init__(self, studcontr, labcontr):
        self.__studcontr = studcontr
        self.__labcontr = labcontr
        
    def menu(self):
        print("0 - Exit")
        print("1 - Add a student")
        print("2 - Add a laboratory")
        print("3 - Find by id")
        print("4 - Find laboratory by id")
        
    def start(self):
        while True:
            self.menu()
            cmd = int(input("Give option: "))
            
            if cmd == 0:
                break
            
            if cmd == 1:
                id = int(input("Give id: "))
                name = input("Give a name: ")
                try:    
                    self.__studcontr.add(id, name)
                except CustomException as msg:
                    print(str(msg))
                print(name + " was saved")
                    
            if cmd ==2:
                studId = int(input("Give id: "))
                labnb = int(input("Give laboratory number: "))
                probnb = input("Give problem desc:")
                try: 
                    self.__labcontr.createLab(studId, labnb, probnb)
                except CustomException as msg:
                    print(str(msg))
                print("Laboratory was added")
            
            if cmd == 3:
                id = int(input("Give student id: "))
                try:
                    s = self.__studcontr.find(id)
                    print(s)
                except CustomException as msg:
                    print(str(msg))
                    
            if cmd == 4:
                id = int(input("Give student id: "))
                try: 
                    l = self.__labcontr.findlab(id)
                    print(l)
                except ValueError as msg:
                    print(msg)
    

          