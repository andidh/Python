'''
Created on Nov 8, 2015

@author: AndiD
'''
class sumDTO():
    def __init__(self,name,lab,grade):
        self.__name=name
        self.__lab=lab
        self.__grade=grade
    
    def get_name(self):
        return self.__name
    def get_lab(self):
        return self.__lab
    def get_grade(self):
        return self.__grade
    
    name = property(get_name, None, None, "Student`s id`s docstring")
    lab  = property(get_lab, None, None, "Lab`s id`s docstring")
    grade = property(get_grade, None, None, "grade's docstring")
   
    def __str__(self):
        return str(self.name) + " " +str(self.lab)+" "+ str(self.grade)
