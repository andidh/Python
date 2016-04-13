'''
Created on Dec 14, 2015

@author: AndiD
'''
class Student:
    """
    A class which creates objects of the type Student
    """
    def __init__(self, student_id, name, group):
        """
        Initialise the class with its state

        :param student_id: an integer > 0 and must be unique
        :param name: string
        :param group: integer > 0
        """
        self._student_id = student_id
        self._name = name
        self._group = group

    def get_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_group(self):
        return self._group

    def set_student_id(self, student_id):
        self._student_id = student_id

    def set_name(self, name):
        self._name = name

    def set_group(self, group):
        self._group = group

    def to_str(self):
        return "{" + str(self._student_id) + ", " + self._name + ", " +str(self._group) + "}"

    def __repr__(self):
        return "{" + str(self._student_id) + ", " + self._name + ", " +str(self._group) + "}"

