'''
Created on Feb 4, 2016

@author: AndiD
'''

class Contact:
    
    def __init__(self, id, name, tel, group):
        self.__id = id 
        self.__name = name
        self.__tel = tel
        self.__group = group
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_tel(self):
        return self.__tel
    
    def get_group(self):
        return self.__group
    
    def __eq__(self, ot):
        return self.get_id() == ot.get_id() and self.get_name() == ot.get_name() and self.get_tel() == ot.get_tel() and self.get_group() == ot.get_group()
    
    id = property(get_id, None, None, None)
    name = property(get_name, None,None, None)
    tel = property(get_tel, None, None, None)
    group = property(get_group, None, None, None)
    
    def __str__(self):
        return str(self.id) + " " + self.name + " " + str(self.tel) + " " + self.group
    
    
def testContact():
    c = Contact("2", "Flori","0741260380",  "Family")
    assert c.get_id()=="2"
    assert c.get_name() == "Flori"
    assert c.get_tel() == "0741260380"
    assert c.get_group() == "Family"
    
testContact()
    