from contr.ControllerException import ControllerException
from domain.Grade import Grade
from repository.Repository import Repository


class RepoWritingFileGrade(Repository):
    def __init__(self, repo_stud, repos_assign):
        Repository.__init__(self)
        self.repo_stud = repo_stud
        self.repo_assign = repos_assign

    def reading(self):
        file = open("/Users/ecaterinacarazan/PycharmProjects/files/grade.txt", "r")
        lines = file.read().splitlines()
        for line in lines:
            list = line.split(", ")
            student = self.repo_stud.get_by_id(int(list[1]))
            assign = self.repo_assign.get_by_id(int(list[2]))
            grade = Grade(int(list[0]), student, assign, int(list[3]))
            for g in Repository.get_all(self):
                if grade.get_id() == g.get_id():
                    raise ControllerException("Can not add grade with same id")
                Repository.add_item(self, grade)
        file.close()

    def writing(self):
        file = open("/Users/ecaterinacarazan/PycharmProjects/files/grade.txt", "w")
        list = Repository.get_all(self)
        for grade in list:
            stud_id = grade.get_student().get_id()
            assign_id = grade.get_assignment().get_id()
            string = str(grade.get_id()) + ", " + str(stud_id) + ", " + str(assign_id) + ", " + str(grade.get_grade())
            file.write(string + "\n")
        file.close()
