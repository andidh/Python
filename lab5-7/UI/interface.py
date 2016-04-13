'''
Created on Nov 2, 2015

@author: AndiD
'''

from Repository.repository import StudentRepo, LabRepo, GradeRepo
from Controller.controller import SController, LController, GController

class UI:
    
    def __init__(self):
        rep=StudentRepo()
        self._ctrs=SController(rep)
        repo=LabRepo()
        self._ctrl=LController(repo)
        repon=GradeRepo()
        self._ctrg=GController(repon,rep,repo)
        
    def printmenu(self):
        print("1 - add student")
        print("2 - remove student")
        print("3 - update student")
        print("4 - search student")
        print("5 - print all students")
        print("6 - add assignment")
        print("7 - remove assignment")
        print("8 - update assignment")
        print("9 - search laboratory")
        print("10 - print all assignments")
        print("11 - give grade")
        print("12 - print all the grades")
        #print("13 - sort by name and grade)
        #print("14 - print students with grades grades average < 5")
        print("0 - Exit")
        
        

    def addstudent(self):
        id = int(input("Give student id: "))
        name = input("Give student name: ")
        group = int(input("Give student group "))
        s = self._ctrs.add(id, name, group)
        print (s.get_name(), "was saved")


    def addlaboratory(self):
        nb = int(input("Give number of laboratory: "))
        description = input("Give description ")
        deadline = input("Give deadline: ")
        p = self._ctrl.add(nb, description, deadline)
        print ("Laboratory was assigned")



    def deletestudent(self):
        id = int(input("Give id: "))
        self._ctrs.deletestud(id)
        print ("Student was removed")


    def searchstudent(self):
        id = int(input("Give id: "))
        print (self._ctrs.findstud(id))



    def deletelaboratory(self):
        nb = int(input("Give the number of the assignment: "))
        self._ctrl.deletelab(nb)
        print ("The assignment was removed")


    def searchlaboratory(self):
        nb= int(input("Give the number of the assignment: "))
        print (self._ctrl.findlab(nb))
        


    def updatestudent(self):
        id = int(input("Give id: "))
        name = input("Give name: ")
        group = int(input("Give group: "))
        s = self._ctrs.upstud(id, name, group)
        print (s.get_name(), "updated")


    def updatelaboratory(self):
        nb = int(input("Give the number of the assignment: "))
        description = input("Description: ")
        deadline = input("Give the deadline of the laboratory: ")
        p = self._ctrl.updatelab(nb, description, deadline)
        print (p.get_number(), "updated")


    def givegrade(self):
        id = int(input("Give id: "))
        nb = int(input("Give assignment: "))
        grade = int(input("Give grade: "))
        self._ctrg.associate(id, nb, grade)
        print ("Grade was given")


    '''def sortstud(self):
        leg = self._ctrg.sor()
        for l in leg:
            print (l)'''
            
    def allstud(self):
        for s in self._ctrs.allstud():
            print(s)

    def alllab(self):
        for l in self._ctrl.alllab():
            return(l)
    
    
    def printgrade(self):
        leg=self._ctrg.getDTO()
        for l in leg:
            print(l)
            
    '''def average(self):
        leg=self._ctrg.avrg()
        for l in leg:
            print(l)'''
            
    def run_ui(self):
        while True:
            self.printmenu()
            opt=int(input("Give command: "))
            if opt==0:
                break
            if opt==1:
                try:
                   self.addstudent()
                except ValueError as msg:
                    print(msg)
            if opt==6:
                try:
                    self.addlaboratory()
                except ValueError as msg:
                    print(msg)
            if opt==2:
                try:
                    self.deletestudent()
                except ValueError as msg:
                    print(msg)
            if opt == 4:
                try:
                    self.searchstudent()
                except ValueError as msg:
                    print(msg)
            if opt == 7:
                try:
                    self.deletelaboratory()
                except ValueError as msg:
                    print(msg)
            if opt == 9:
                try:
                    self.searchlaboratory()
                except ValueError as msg:
                    print(msg)
            if opt == 3:
                try:
                    self.updatestudent()
                except ValueError as msg:
                    print(msg)
            if opt == 8:
                try:
                    self.updatelaboratory()
                except ValueError as msg:
                    print(msg)
            if opt == 11:
                try:
                    self.givegrade()
                except ValueError as msg:
                    print(msg)
            if opt == 12:
                self.printgrade()
                
            '''if opt == 13:
                self.eleviordonati()'''
                
            if opt == 5:
                print(self.allstud())
                
            if opt==10:
                print(self.alllab())
            '''if opt==14:
                self.average()'''
                
            
c=UI()
c.run_ui()
            