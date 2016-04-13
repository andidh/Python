'''
Created on Dec 20, 2015

@author: AndiD
'''

from domain.Validator import *
from repository.FileRepo import StudentFileRepo
from repository.LabFileRepo import *
from controller.StudentController import *
from controller.LabController import *
from console.UI import *
 
class App:
    
    def main(self):
        StudRepo = StudentFileRepo("student.txt")
        StudContr = StudentController(StudRepo, StudentValidator)
        
        
        print(StudRepo)
        labrep = LabRepo("laboratory.txt", StudRepo)
        LabContr = LabController(labrep, StudRepo)
        
        print(labrep)
        
        cons = UI(StudContr, LabContr)
        cons.start()
    
    
run = App()
run.main()
        
        
