'''
Created on Dec 14, 2015

@author: AndiD
'''
from contr.ControllerException import ControllerException


class ValidatorAssign:

    def __init__(self):
        pass

    def validate_assignment(self, assignment):
        """
        validate the assignment by positive id

        :param assignment:
        :return:
        """
        if assignment.get_id() < 0:
            raise ControllerException("Id should be positive")
