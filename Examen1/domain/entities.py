


class Example:
    
    def __init__(self, sent):
        
        self.__sent = sent
                
    def get_atr1(self):
        return self.__sent
    

    def __eq__(self, other):
        return self.get_atr1() == other.get_atr1() 
    
    
    sent = property(get_atr1, None, None, None)
    
    def __str__(self):
        return str(self.sent) 