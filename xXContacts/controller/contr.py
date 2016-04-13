'''
Created on Feb 4, 2016

@author: AndiD
'''

from domain.entities import Contact

class Controller:
    
    def __init__(self, repo, val):
        self.repo = repo
        self.val = val
        
    
    def searchName(self, name):
        return self.repo.searchName(name)
    
    def add(self, id, name, tel, group):
        contact = Contact(id, name, tel, group)
        self.val.validate(contact)
        self.repo.add(contact)
        
    def group(self, group):
        return self.repo.group(group)
    
    def export(self, file):
        return self.repo.export(file)
    
    