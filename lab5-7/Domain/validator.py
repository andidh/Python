class StoreError(Exception):
    def __init__(self, message=None, ex=None):
        Exception.__init__(self, message)
        self.__ex = ex
        self.__message = message
    
    @property
    def message(self):
        msg = self.__message if self.__message else ""
        if self.__ex is None:
            return msg
        msg = msg + type(self.__ex).__name__ + ": " + str(self.__ex)
        return msg
     
    def __str__(self):
        return self.message

class ValidatorError(StoreError):
    pass

class StudentValidator(object):
    def validateS(self, student):
        errors = []
        if not type(student.Id) is int or student.Id < 0 :
            errors.append("Id must be a natural number")
        if not student.Id:
            errors.append("Id does not exist")    
        if not student.name:
            errors.append("The name can not be empty")
        if not student.group:
            errors.append("The group can not pe empty")
        if len(errors) > 0:
            raise ValidatorError(str(errors)) 

class LaboratorValidator(object):
    def validateL(self, lab):
        errors = []
        if not type(lab.Id) is int or lab.Id < 0:
            errors.append("Id must be a natural number")
        if not lab.description:
            errors.append("Description can not be empty")
        if not lab.deadline:
            errors.append("Deadline can not be empty")
        if len(errors) > 0:
            raise ValidatorError(str(errors))
        
class NotaValidator(object):
    def validateN(self, grade):
        errors=[]
        if grade.get_stud()==None:
            errors.append("Student does not exist")
        if grade.get_lab()==None:
            errors.append("Lab does not exist")
        if grade.get_grade()==None:
            errors.append("Grade does not exist")
        if len(errors) > 0:
            raise ValidatorError(str(errors))
      

