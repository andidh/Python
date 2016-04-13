'''
Created on Nov 8, 2015

@author: AndiD
'''
from UI.console import UI
from Controller.CLaboratory import LaboratoryController
from Controller.CGrade import GradeController
from Controller.CStudent import StudentController
from Repository.Repos import  *
from Domain.validator import StudentValidator, LaboratorValidator, NotaValidator


class App(object):
    
    
    def main(self):
        sc=StudentController(SLRepo(StudentValidator()))
        
        lc=LaboratoryController(SLRepo(LaboratorValidator()))
        
        nr=GradeRepo(NotaValidator())
        cc=GradeController(nr,SLRepo(LaboratorValidator()), SLRepo(StudentValidator()))

        cons = UI(sc,lc,cc)
        cons.startUI()
    

app = App()
app.main()
