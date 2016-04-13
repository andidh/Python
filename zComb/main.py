'''
Created on Feb 5, 2016

@author: AndiD
'''
from repository.Srepo import *
from controller.Scntr import *
from console.UI import *
from repository.Grepo import Grepo
from controller.Gcntr import *

def app():
    
    srepo = SRepo("stud.txt")
    grepo = Grepo(srepo, "grade.txt")
    scntr = SController(srepo)
    gcntr = GradeController(grepo, srepo)
    ui = UI(scntr, gcntr)
    
    ui.start()
    
    
app()