'''
Created on Feb 4, 2016

@author: AndiD
'''

from repository.repo import ContactRepo
from controller.contr import *
from console.ui import *
from domain.validator import Validate

def app():
    
    repo = ContactRepo("ct.txt")
    val = Validate()
    cntr = Controller(repo, val)
    ui = UI(cntr)
    
    ui.start()
    
app()