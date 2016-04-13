from contr.ControllerException import ControllerException
from domain.Assignment import Assignment
from repository.Repository import Repository


class RepoWritingFileAssign(Repository):
    def __init__(self):
        Repository.__init__(self)

    def reading(self):
        file = open("/Users/ecaterinacarazan/PycharmProjects/files/assignment.txt", "r")
        lines = file.read().splitlines()
        for line in lines:
            list = line.split(", ")
            assign = Assignment(int(list[0]), list[1], list[2])
            for asgn in Repository.get_all(self):
                if asgn.get_id() == int(list[0]):
                    raise ControllerException("Can not add assignment with same id")
            Repository.add_item(self, assign)
        file.close()

    def writing(self):
        file = open("/Users/ecaterinacarazan/PycharmProjects/files/assignment.txt", "w")
        list = Repository.get_all(self)
        for assign in list:
            string = str(assign.get_id()) + ", " + str(assign.get_deadline()) + ", " + str(assign.get_description())
            file.write(string + "\n")
        file.close()

