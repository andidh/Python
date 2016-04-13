'''
Created on Nov 2, 2015

@author: AndiD
'''
class Student:
    
    def __init__(self, newid, newname, newgroup):
        '''Creates an student characterized by Id, name and group 
        Input: id - integer, name - string, group - integer'''

        self.__id = newid
        self.__name =  newname
        self._group =  newgroup
        
    def get_id(self):
        
        return self._id
    
    def get_name(self):
        
        return self.__name
    
    def set_name(self, value):
        
        self.__name = value
        
    def get_group(self):
        
        return self.__group
    
    def set_group(self, value):
        
        self.__group = value 
        
    Id = property(get_id, None, None, "Student id's docstring")
    name = property(get_name, set_name, None, "name's docstring")
    group = property(get_group, set_group, None, "group's docstring")
    
    def __str__(self):
        
        return str(self.Id) +  " "  + self.name + " " + str(self.group)
    
class Laboratory:
        
    def __init__(self, nb, description, deadline):
        
        self.__nb=nb
        self.__description= description
        self.__deadline = deadline
        
    def get_number(self):
        
        '''Returns the number of laboratory and problem, as well'''    
        return self.__nb
    
    def get_description(self):
        
        '''Returns the description of the problem'''
        return self.__description
    
    def get_deadline(self):
        
        '''Returns the deadline of the assignment'''
        return self.__deadline
    
    def set_description(self, value):
        
        self.__description =  value
        
    def set_deadline(self, value):
        
        self.__deadline = value
      
    Id = property(get_number, None, "Lab id's docstring")
    description = property(get_description, set_description, None, "Description's docstring")
    deadline = property(get_deadline, set_deadline, None, "Deadline's dosctring")
    
    def __str__(self):
        
        return str(self.Id) + " " + self.description + " " + str(self.deadline)
    
class Grade: 
    
    def __init__(self, stud, lab, grade):
        self.__stud = stud
        self.__lab = lab
        self.__grade = grade
        
    def get_stud(self):
        return self.__stud
    
    def get_lab(self):
        return self.__lab
    
    def get_grade(self):
        return self.__grade
    
    student = property(get_stud, None, None, "Student's docstring")
    lab = property (get_lab, None, None, "Lab's dosctring")
    grade = property (get_grade, None, None, "Grade's docstring")
    
    def __str__(self):
        return str(self.student) + " " +  str(self.lab) + " " + str(self.grade)
    