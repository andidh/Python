'''
Created on Nov 26, 2015

@author: AndiD
'''

from Domain.Entities import *
from Domain.Validator import *
from Repository.Repo import *
from Controller.Controller import *
from Console.UI import *

class App():
    
    def main(self):
        clrep = ClientRepo()
        clval = ClientValidator()
        clcntr = ClientController(clrep, clval)
        
        st = UI(clcntr)
        st.start()
        
        

app = App()
app.main()
