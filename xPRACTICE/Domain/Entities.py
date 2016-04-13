'''
Created on Nov 25, 2015

@author: AndiD
'''

class Client():
    
    def __init__(self, id, name, cnp):
        self._id = id
        self._name = name
        self._cnp = cnp
        
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name

    def get_cnp(self):
        return self._cnp
    
    def set_name(self, value):
        self._name = value
        
    def set_cnp(self, value):
        self._cnp = value
    
class Movie():
    
    def __init__(self, id, title, description, type):
        self.__id = id
        self.__title = title
        self.__description= description
        self.__type = type
        
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description
    
    def get_type(self):
        return self.__type
    
    def set_title(self, value):
        self.__title = value
        
    def set_description(self, value):
        self.__description = value
        
    def set_type(self, value):
        self.__type = value
    
    
        
def testClient():
    c=Client(1, "Andi", 21312)
    assert c.get_id() == 1
    assert c.get_name() == "Andi"
    assert c.get_cnp() == 21312
    
def testMovie():
    pass