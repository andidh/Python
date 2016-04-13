'''
Created on Feb 6, 2016

@author: AndiD
'''
from repository.repo import Repository
from domain.validator import Validator
from console.UI import UI
from controller.contr import Controller

def app():
    
    repo = Repository("prod.txt")
    val = Validator()
    cntr = Controller(repo, val)
    ui = UI(cntr)
    
    ui.start()
    
    
app()
