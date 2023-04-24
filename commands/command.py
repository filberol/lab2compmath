class Command:
    def __init__(self, state_manager=None):
        self.state_manager = state_manager

    def execute_command(self, arguments):
        print("This command was not yet implemented.")
        print(self.state_manager)

    def __str__(self):
        return "Basic command interface"
