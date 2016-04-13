'''
Created on Feb 6, 2016

@author: AndiD
'''

from domain.entities import Product
from domain.validator import Validator
from repository.repo import Repository
from controller.contr import Controller


    
def testDomain():
    p = Product("1", "Sugar", "100", "8")
    assert p.get_id() == "1"
    assert p.get_name() == "Sugar"
    assert p.get_quantity() == "100"
    assert p.get_price() == "8"
    
testDomain()

def testValidator():
    v = Validator()
    p = Product("1", "sugar", "-100", "9")
    try:
        v.validate(p)
        return False
    except ValueError as err:
        print(err)
        
testValidator()


def testRepo():
    r = Repository("testprod.txt")
    p = Product("1", "sugar", "100", "3")
    r.add(p)
    assert len(r) == 1
    
testRepo()

def testController():
    ac=Controller()
    assert ac.add("2",'Sugar','740','3')==False
    assert ac.addContact('1','Name3','321','2')==False
    assert ac.addContact('3','Name3','4353223','31r')==False
    ac.addCart('1', '100')
    assert ac.showIncome() == '100'
    list=ac.returnAll()

    
