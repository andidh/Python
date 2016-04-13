'''
Created on Dec 7, 2015

@author: AndiD
'''
class Repository:
    """
    Repository for storing IDObject instances
    """
    def __init__(self):
        self.__list = []

    def add(self, anElem):
        if self.find(anElem.get_type(), anElem.get_brand()) != None:
            raise ValueError("Product already added")
        self.__list.append(anElem)

    def update(self, anElem):
        """
        Input: list, anElem
                list - the elements in the repository
                anElem - The element that will be updated
        Output: list
            - list with the same element id modified by anElem
        Raises ValueError in case the element is not in the repository
        """
        el = self.find(anElem.get_type(), anElem.get_brand())
        if el == None:
            raise ValueError("Element not found!")
        if anElem.get_quantity() == el.get_quantity():
            raise ValueError("There are not enough products of the given type and brand")
        else:
            indexOfAnElem = self.__list.index(el)
            self.__list.remove(el)
            self.__list.insert(indexOfAnElem, anElem)
        
    def find(self, type, brand):       
        for e in self.__list:        
            if (str(e.get_type())==str(type)) and (str(e.get_brand()) == str(brand)):        
                return e
        return None     

    
    def getAll(self):
        return self.__list
    
    def __str__(self):
        r = "Elements from Repository:\n"
        for e in self.__list:
            r += str(e)
            r += "\n"
        return r



def testUpdate():
    type = "Tablet"
    brand = "Samsung"
    quantity = "3"
    c = Repository()
    assert c.update(type, brand, quantity) == ["Tablet" "Samsung" "3"]