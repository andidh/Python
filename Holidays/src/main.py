from Console.Colsole import Console
from Controller.Controller import Controller
from Repository.FileRepository import FileRepository

__author__ = 'ecaterinacarazan'


def main():
    repository = FileRepository()
    controller = Controller(repository)
    console = Console(controller)
    console.pre_run()

main()
