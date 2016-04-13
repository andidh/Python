class Grade:
    """
    A class which creates objects of the type Grade
    """
    def __init__(self, grade_id, student, assignment, grade):
        """
        initialize the grade class

        """
        self._grade_id = grade_id
        self._student = student
        self._assignment = assignment
        self._grade = grade

    def get_id(self):
        return self._grade_id

    def get_student(self):
        return self._student

    def get_assignment(self):
        return self._assignment

    def get_grade(self):
        return self._grade

    def set_student(self, student):
        self._student = student

    def set_assign(self, assign):
        self._assignment = assign

    def set_grade(self, grade):
        self._grade = grade

    def __repr__(self):
        return "{" + self._student.to_str() + ", " + self._assignment.to_str() + ", " + str(self._grade_id) + ", " + str(self._grade) + "}"