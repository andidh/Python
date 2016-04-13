 
 
 
from Repository.FileRepo import *
from Controller.ProductController import *
from UI.StoreUI import *
 
class App(object): 
    def main(self):
        
        ProdRepo = ProductRepository("products.txt")
        ProdContr = ProductController(ProdRepo)
        
        cons = UI(ProdContr)
        cons.start_ui()
        

productapp= App()   
productapp.main()

