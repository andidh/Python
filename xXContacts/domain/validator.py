'''
Created on Feb 4, 2016

@author: AndiD
'''

from domain.entities import Contact
class Validate:
    
    def validate(self, c):
        err = []
        if c.get_name() == "":
            err.append("Name cannot be empty")
        if c.get_group() != "friends" and c.get_group()!="family":
            err.append("Group must be one of: friends, family")
        if c.get_tel() == "":
            err.append("Phone cannot pe empty")
        if len(err) > 0:
            raise ValueError(err)
        
