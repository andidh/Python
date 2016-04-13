'''
Created on Nov 16, 2015

@author: AndiD
'''

class Student:
    def __init__(self, student_id, name, group):
        """

        :param student_id:
        :param name:
        :param group:
        :return:
        """
        self._student_id = student_id
        self._name = name
        self._group = group

    def get_student_id(self):
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

    def __repr__(self):
        return "{" + str(self._student_id) + ", " + self._name + ", " +str(self._group) + "}"

