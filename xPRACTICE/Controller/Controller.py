'''
Created on Nov 25, 2015

@author: AndiD
'''
from Domain.Entities import Client, Movie
from Domain.Validator import *
from Repository.Repo import *

class ClientController:
    
    def __init__(self, rep, val):
        self.__rep = rep
        self.__val = val
        
    def addClient(self, id, name, cnp):
        c = Client(id, name, cnp)
        self.__val.validcl(c)
        self.__rep.store(c)
        return c


def testRepoClient():
    val = ClientValidator()
    rep = ClientRepo()
    cntr = ClientController(rep, val)
    acl = cntr.addClient(1, "Andi", 3928492)
    assert acl.get_name() == "Andi"
    assert acl.get_id() == 1
    try:
        cl = cntr.addClient(1, "Maria", 487894)
        assert False
    except ValueError:
        assert True
    try :
        cl2 = cntr.addClient(3, "", 4970932)
        assert False
    except ValueError:
        assert True
    
#testRepoClient()