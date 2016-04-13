'''
Created on Nov 2, 2015

@author: AndiD
'''
class Student:
    
    def __init__(self, newid, newname, newgroup):
        '''Creates an student characterized by Id, name and group 
        Input: id - integer, name - string, group - integer'''

        self._id = newid
        self._name =  newname
        self._group =  newgroup
        
    def get_id(self):
        
        return self._id
    
    def get_name(self):
        
        return self._name
    
    def set_name(self, value):
        
        self_name = value
        
    def get_group(self):
        
        return self._group
    
    def set_group(self, value):
        
        self._group = value 
        
    
    
    def __str__(self):
        
        return str(self._id) +  " "  + self._name + " " + str(self._group)
    
class Laboratory:
        
    def __init__(self, nb, description, deadline):
        
        self._nb=nb
        self._description= description
        self._deadline = deadline
        
    def get_number(self):
        
        '''Returns the number of laboratory and problem, as well'''    
        return self._nb
    
    def get_description(self):
        
        '''Returns the description of the problem'''
        return self.__description
    
    def get_deadline(self):
        
        '''Returns the deadline of the assignment'''
        return self._deadline
    
    def set_description(self, value):
        
        self._description =  value
        
    def set_deadline(self, value):
        
        self._deadline = value
    
    def __str__(self):
        
        return str(self._nb) + " " + self._description + " " + str(self._deadline)
    
class Grade: 
    
    def __init__(self, stud, lab, grade):
        self._stud = stud
        self._lab = lab
        self._grade = grade
        
    def get_stud(self):
        return self._stud
    
    def get_lab(self):
        return self._labb
    
    def get_grade(self):
        return self._note
    
    def __str__(self):
        return str(self._student) + " " +  str(self._lab) + " " + str(self._grade)
    