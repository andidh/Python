'''
Created on Dec 14, 2015

@author: AndiD
'''

from contr.ControllerException import ControllerException


class ValidatorGrade:

    def __init__(self):
        pass

    def validate_grade(self, grade):
        """
        validate the grade by grade between 0 and 10, id > 0
        :param grade:
        :return:
        """
        if grade.get_id() < 0:
            raise ControllerException("Id should be positive")
        if grade.get_grade() < 0 or grade.get_grade() > 10:
            raise ControllerException("Grade is a number between 0 and 10")

