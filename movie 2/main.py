'''
Created on Dec 5, 2015

@author: AndiD
'''
from Repository.Repo import *
from Repository.FileRepo import *
from Controller.Contr import *
from Console.UI import *
from Domain.Validator import *



def main():
    mrepo = FileMovie("MovieFile.txt")
    val = ValidatorMovie()
    mctrl = MovieController(val, mrepo)
    print("---> Initial state of repositories --movie")
    print(mrepo)
    
    run = UI(mctrl)
    run.start()

main()