class Assignment:
    """
    A class which creates objects of the type Assignment
    """
    def __init__(self, assignment_id, description, deadline):
        """
        Initialise the class with its state
        :param assignment_id: an integer >0, must be unique
        :param description: string
        :param deadline: string
        """
        self._assignment_id = assignment_id
        self._deadline = deadline
        self._description = description

    def get_id(self):
        return self._assignment_id

    def get_deadline(self):
        return self._deadline

    def get_description(self):
        return self._description

    def set_deadline(self, deadline):
        self._deadline = deadline

    def set_description(self, description):
        self._description = description

    def set_id(self, id):
        self._assignment_id = id

    def to_str(self):
        return "{" + str(self._assignment_id) + ", " + self._description + ", " + self._deadline + " }"

    def __repr__(self):
        return "{" + str(self._assignment_id) + ", " + self._description + ", " + self._deadline + " }"


