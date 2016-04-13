from console.Console import Console
from contr.Controller import Controller
from contr.Validator import Validator
from repos.Repository import Repository



def main():
    validator = Validator()
    repo = Repository()
    controller = Controller(repo, validator)
    console = Console(controller)
    console.run()

    # console = Console(Controller(Repository(), Validator()))
    # console.run()

main()