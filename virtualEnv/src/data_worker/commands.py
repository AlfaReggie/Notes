class Commands:

    def __init__(self, commands: list):
        self.commands = commands

    def __str__(self):
        result_str = f"\nCommands: "
        for i, command in enumerate(self.commands):
            result_str += f"\n{i + 1}: {command}"
        return result_str

    def check_command(self, number_command: int):
        if len(self.commands) >= int(number_command) & number_command > 0:
            return int(number_command)
        print("Nor found command!")
        return False