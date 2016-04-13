'''
Created on Dec 14, 2015

@author: AndiD
'''

from contr.ControllerException import ControllerException


class ValidatorStudent:

    def __init__(self):
        pass

    def validate_student(self, student):
        """
        validate the student by id > 0 , group > 0, name non void
        :param student:
        :return:
        """
        if student.get_id() < 0:
            raise ControllerException("Id should be positive")
        if student.get_group() < 0:
            raise ControllerException("Group number should be positive")
        if student.get_name() == "":
            raise ControllerException("Name can not be empty")

