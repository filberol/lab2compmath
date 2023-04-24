from commands import *
from functions import *
from state_manager import StateManager
from terminal_colors import *


def read_command(command_dict):
    input_line = input("-> ").split(" ")
    command_line = input_line.pop(0)
    try:
        command_dict[command_line].execute_command(input_line)
    except KeyError:
        print_c("Unknown command.", Colors.FAIL)


if __name__ == '__main__':
    functions = [
        module.ModuleFunction(),
        sinus.SinusFunction(),
        exponent.ExpFunction(),
        polynom.PolFunction()
    ]
    manager = StateManager(functions)
    commands = {
        "exit": exit.Exit(),
        "pwd": pwd.Pwd(),
        "show": show.ShowPic(),
        "list": list.ListFunctions(manager),
        "help": comm_list.ShowCommands(manager),
        "solve": solve.SolveFunction(manager),
        "cross": cross.CrossFunctions(manager)
    }
    manager.set_commands(commands)
    while True:
        read_command(commands)
