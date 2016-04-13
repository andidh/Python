'''
Created on Dec 5, 2015

@author: AndiD
'''

def openFileCreateIfNeeded(nameF):
    try: 
        fh = open(nameF, "r")
    except FileNotFoundError:
        fh = open(nameF, "w")
        fh.close()
        fh = open(nameF, "r")
        
def readAllFileContent(nameF):
    fh = openFileCreateIfNeeded(nameF)
    rez = fh.read()
    fh.close()
    return rez 

def createEmptyFIle(nameF):
    fh = open(nameF, "w")
    fh.close()
        