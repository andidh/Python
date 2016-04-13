from repository.repo import Repository
from console.UI import UI
from controller.contr import Controller

def app():
    
    repo = Repository("file.txt")
    cntr = Controller(repo)
    ui = UI(cntr)
    
    ui.start()
    
    
app()
