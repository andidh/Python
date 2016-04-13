'''
Created on Dec 7, 2015

@author: AndiD
'''
def openFileCreateIfNeeded(nameF):
    """
    Deschide un fisier pentru citire
    Daca nu exista fisierul atunci se creeaza un fisier gol
    """
    try:
        fH = open(nameF, "r")
    except FileNotFoundError:
        #daca nu exista fisierul il cream acum
        fH = open(nameF, "w")
        fH.close()    
        fH = open(nameF, "r")
    return fH


def readAllFileContent(nameF):
    """
    Citeste continutul unui fisier
    """
    fH = openFileCreateIfNeeded(nameF)
    rez = fH.read()
    fH.close()
    return rez

def createEmptyFile(nameF):
    """
    creeaza un fisier nou
    daca fisierul exista, atunci este golit
    """
    fH = open(nameF, "w")
    fH.close()