'''
Created on Nov 21, 2015

@author: AndiD
'''
from Repository.repo import RepositoryStudent
from Controller.contr import StudentController

class UI:
    
    def __init__(self):
        rep = RepositoryStudent()
        self.__ctrs = StudentController(rep)
        
    def menu(self):
        print("1 - add student")
        print("2 - remove student")
        print("3 - update student")
        print("4 - search student")
        
    def addStud(self):
        id = int(input("Give an id: "))
        name = input("Give a name: ")
        group = int(input("give a group: "))
        self.__ctrs.addS(id, name, group)
        
        
    def runUI(self):        
        while True:
            self.menu()
            opt=int(input("Give command: "))
            if opt==0:
                break
            if opt==1:
                self.addStud()
                
                
c= UI()
c.runUI()
                