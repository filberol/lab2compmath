from commands.command import Command
import os


class Pwd(Command):
    def __init__(self):
        Command.__init__(self)

    def execute_command(self, arguments):
        print(os.getcwd())

    def __str__(self):
        return "Show current working folder"
