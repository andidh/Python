'''
Created on Feb 4, 2016

@author: AndiD
'''
from domain.entities import Contact
from _operator import attrgetter

class ContactRepo:
    
    def __init__(self, file):
        
        self.list = []
        self.file = file
        self.__loadFromFile()
        
    def getAll(self):
        return self.list
    
    
    def add(self, contact):
        self.list.append(contact)
        self.__writeToFile(contact)
    
    def __loadFromFile(self):
        f = open(self.file, "r")
        for line in f:
            id, name, tel, group = line.split(",")
            contact = Contact(id, name, tel, group)
            self.list.append(contact)
        f.close()
        
    def __writeToFile(self, contact):
        f = open(self.file, "a")
        line = str(contact.get_id()) + "," + contact.get_name() + "," + str(contact.get_tel()) + "," + contact.get_group() + "\n"
        f.writelines(line)
        f.close()
        
    def searchName(self, name):
        done = 0
        for c in self.list:
            if c.get_name() == name: 
                done += 1
                print(c)
        if done == 0:
            print("Contact does not exist")
    
    def group(self, group):
        rez = []
        for c in self.list:
            if c.get_group().strip() == group:
                rez.append(c)
        rez = sorted(rez, key = attrgetter('name'))
        return rez
                
                
    def export(self, file):
        f = open(file, "w")
        for c in self.list:
            line = c.get_name() + "," + str(c.get_tel()) + "\n"
            f.writelines(line)
        f.close()
        

    