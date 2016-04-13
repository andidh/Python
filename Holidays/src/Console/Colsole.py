from Exceptions.Exception import CustomException

__author__ = 'ecaterinacarazan'

class Console:
    def __init__(self, controller):
        self.controller = controller

    def filterType(self):
        type = input("give type:")
        try:
            for hol in self.controller.filterByType(type):
                print(hol)
        except CustomException as e:
            print(e.get_msg())

    def filterResort(self):
        resort = input("give resort")
        try:
            for hol in self.controller.filterByResort(resort):
                print(hol)
        except CustomException as e:
            print(e.get_msg())

    def print_all(self):
        for hol in self.controller.get_all():
            print(hol)

    def menu(self):
        print("1 - filter by type")
        print("2 - filter by resort")
        print("3 - print all")
        print("0 - exit")

    def run(self):
        option = {1: self.filterType, 2: self.filterResort, 3: self.print_all}
        while True:
            self.menu()
            opt = int(input("option:"))
            if opt == 0:
                self.write()
                exit(0)
            try:
                option[opt]()
            except ValueError:
                print("Wrong input")
            except KeyError:
                print("Option not implemented")

    def read(self):
        self.controller.read()
        self.run()

    def write(self):
        self.controller.write()

    def pre_run(self):
        self.read()
