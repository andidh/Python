
from domain.entities import Example
class Repository:
    
    def __init__(self, file):
        
        self._file = file
        self.list = []
        
        self.loadFromFile()
        
    
    
    
    def add(self, e): 
        '''
        Function which adds a product to the file
        e = object of type E
        ''' 
        self.list.append(e)
        self.__storeToFile(e)
    
    
    
    
    def loadFromFile(self):
        
        '''
        Function which loads the products from the file 
        output : file.txt
        
        '''
        f = open(self._file, "r")
        list1 = []
        for line in f:
            list1.append(line.split(" "))
            self.list.append(list1)
        f.close()
            
    def __storeToFile(self, e):
        '''
        Function which stores the products to the file
        '''
        f = open(self._file, "a")
        list1 = []
        list1.append(e.split(" "))
        for i in range (0, len(list1)):
            line = str(list1[i]) + " " 
        line += "\n"
        f.writelines(line)
        f.close()
        
        
    def __len__(self):
        return len(self.list)
    
    def getAll(self):
        return self.list