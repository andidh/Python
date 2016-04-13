'''
Created on Feb 3, 2016

@author: AndiD
'''
from Repository.Filerepo import File
from Controller.Controller import Controller
from Console.Console import Console


def start():
    
    repo = File("products.txt")
    cntr = Controller(repo)
    ui = Console(cntr)
    
    ui.start()
    
start()