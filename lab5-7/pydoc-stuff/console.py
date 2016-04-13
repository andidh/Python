'''
Created on Nov 14, 2015

@author: AndiD
'''

from validator import StoreError
from Repos import *
from CStudent import  *
from CGrade import *
from CLaboratory import *


class UI:
    
    def __init__(self, StudentController, LaboratoryController, GradeController):
        self.__controllerS=StudentController
        self.__controllerL=LaboratoryController
        self.__controllerG=GradeController
        
    def Meniu(self): 
        print("0.Exit") 
        print("1.Add a student")
        print("2.Add laboratory")
        print("3.Print all students")
        print("4.Print all laboratories")
        print("5.Delete student")
        print("6.Delete laboratory")
        print("7.Find student")
        print("8.Find laboratory")
        print("9.Update student")
        print("10.Update laboratory")
        print("11.Assign student-laboratory")
        print("12.Print all assignments")
        print("13.Print sorted list of students")
        print("14.Print students with grades average <5")
        
     
    def PrintStud(self, Id):
        Id = int(input("Give id: "))
        name = input("Give name: ")
        group =int(input("Give group: "))
        try:
            self.__controllerS.add_student(Id, name, group)
            print(name, "was successfully added.")
        except StoreError as ve:
            raise StoreError(ex=ve)
        
    def PrintLab(self, Id):
        Id = int(input("Give the number of the Laboratory: "))
        description = input("Give a description ")
        deadline = input("Give deadline: ")
        try:
            self.__controllerL.add_Laboratory(Id, description, deadline)
            print("Laboratory was successfully added.")
        except StoreError as ve:
            raise StoreError(ex=ve)


    def PrintAllStudents(self):
        s = self.__controllerS.getAllStudents()
        for x in s:
            print(x)

    def PrintAllLaboratories(self):
        l = self.__controllerL.getAllLabs()
        for x in l:
            print(x)

    def DeleteStudent(self):
        Id = int(input("Give id:"))
        try:
            self.__controllerS.delete_student(Id)
            self.PrintAllStudents()
        except StoreError as ve:
            raise StoreError(ex=ve)
        
        
    def DeleteLab(self):
        Id = int(input("Give the number of lab:"))
        try:
            self.__controllerL.delete_Laboratory(Id)
            self.PrintAllLaboratories()
        except StoreError as ve:
            raise StoreError(ex=ve)


    def FindStudent(self):
        Id = int(input("Give id: "))
        try:
            s = self.__controllerS.find_student(Id)
            print(s)
        except StoreError as ve:
            raise StoreError(ex=ve)
     
    def findLab(self):
        Nr = int(input("Give the number of lab: "))
        try:
            l = self.__controllerL.find_lab(Nr)
            print(l)  
        except StoreError as ve:
            raise StoreError(ex=ve) 
        
    def UpdateStudent(self):
        Id = int(input("Give id: "))
        name = input("Give name: ")
        group = int(input("Give group:"))
        try:
            self.__controllerS.update_student(Id, name, group)
            self.PrintAllStudent()
        except StoreError as ve:
            raise StoreError(ex=ve)
        
    def UpdateLaboratory(self):
        Id = int(input("Give id: "))
        description = input("Give description: ")
        deadline = input("Give deadline:")
        try:
            self.__controllerL.update_lab(Id, description, deadline)
            self.PrintAllLaboratories()
        except StoreError as ve:
            raise StoreError(ex=ve)


    def PrintGrades(self):
        Id = int(input("Give id student:"))
        Nr = int(input("Give the number of assignment:"))
        grade = int(input("Give grade:"))
        try:
            self.__controllerG.associate(Id, Nr, grade)
            print(self.__controllerS.find_student(Id), "has grade ", grade , " for laboratory number ", Nr)
        except StoreError as ve:
            raise StoreError(ex=ve)


    def PrintAllGrades(self):
        assign = self.__controllerG.getDTOs()
        for l in assign:
            print(l)


    def Sort(self):
        legaturi = self.__controllerG.sort()
        for l in legaturi:
            print(l)
        

    def avrg5(self):

        lista = self.__controllerG.avrg()
        for l in lista:
            print(l)
            



    def startUI(self):
        while True:
            self.Meniu()
            cmd=int(input("Give option: "))
            if cmd==0:
                break
            if cmd==1:
                try:
                    self.PrintStud(id)
                except StoreError as ex:
                    print(ex)
            if cmd==2:
                try:
                    self.PrintLab(id)
                except StoreError as ex:
                    print(ex)
            if cmd==3:
                self.PrintAllStudent()
            if cmd==4:
                self.PrintAllLaboratorie()
            if cmd==5:
                try:
                    self.DeleteStudent()
                except StoreError as ex:
                    print(ex)
            if cmd==6:
                try:
                    self.DeleteLab()
                except StoreError as ex:
                    print(ex)
            if cmd==7:
                try:
                    self.FindStudent()
                except StoreError as ex:
                    print(ex)       
            if cmd==8:
                try:
                    self.findLab()()
                except StoreError as ex:
                    print(ex)
                    
            if cmd==9:
                try:
                    self.UpdateStuden()
                except StoreError as ex:
                    print(ex)
            if cmd==10:
                try:
                    self.UpdateLaborator()
                except StoreError as ex:
                    print(ex)
            if cmd==11:
                try:
                    self.PrintGrade()
                except StoreError as ex:
                    print(ex)
            if cmd==12:
                self.PrintAllGrade()
            if cmd==13:
                self.Sor()
            if cmd==14:
                self.avrg()
