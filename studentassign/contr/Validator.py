'''
Created on Nov 16, 2015

@author: AndiD
'''

from contr.ControllerException import ControllerException


class Validator:

    def __init__(self):
        """
        pass
        :return:
        """
        pass

    def validate_student(self, student):
        if student.get_student_id() < 0:
            raise ControllerException("Id should be positive")
        if student.get_group() < 0:
            raise ControllerException("Group number should be positive")
        if student.get_name() == "":
            raise ControllerException("Name can not be empty")

    def validate_assignment(self, assignment):
        if assignment.get_assignment_id() < 0:
            raise ControllerException("Id should be positive")
        if assignment.get_grade() < 0 or assignment.get_grade() > 10:
            raise ControllerException("Grade should be positive and not greater than 10")
        if assignment.get_student_id() < 0:
            raise ControllerException("Id should be positive")
        
        
def testvalid():
    s=(-1, "Andi" , 45)
    c = Validator()
    try:
        c.validate_student(s)
        assert False
    except ValueError:
        assert True
        
