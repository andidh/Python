'''
Created on Nov 16, 2015

@author: AndiD
'''


class Assignment:
    def __init__(self, assignment_id, student_id, description, deadline, grade):
        """
        Create a new assignment with the following fields:
        :param assignment_id: integer > 0
        :param student_id: integer > 0
        :param description: string
        :param deadline: string
        :param grade: integer 0 < i < 10
        :return:
        """
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._deadline = deadline
        self._description = description
        self._grade = grade

    def get_assignment_id(self):
        return self._assignment_id

    # def set_assignment_id(self, id):
    #     self._assignment_id = id

    def get_student_id(self):
        return self._student_id

    def get_deadline(self):
        return self._deadline

    def get_description(self):
        return self._description

    def get_grade(self):
        return self._grade

    def set_student_id(self, student_id):
        self._student_id = student_id

    def set_deadline(self, deadline):
        self._deadline = deadline

    def set_description(self, description):
        self._description = description

    def set_grade(self, grade):
        self._grade = grade

    def __repr__(self):
        return "{" + str(self._assignment_id) + ", " + str(self._student_id) + ", " + self._description + ", " + self._deadline + ", " + \
               str(self._grade) + "}"

