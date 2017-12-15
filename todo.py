from sys import argv


class Controller:
    def __init__(self, name):
        self.name = name
        if len(argv) == 1:
            Display.print_help(display)
        elif argv[1] == "-l":
            self.list_tasks()
        elif argv[1] == "-lu":
            self.list_tasks()
        elif argv[1] == "-ld":
            self.list_tasks()
        elif argv[1] == "-a":
            self.new_task()
        elif argv[1] == "-r":
            self.remove_task()
        elif argv[1] == "-c":
            self.complete_task()
        elif argv[1] == "-uc":
            self.complete_task()
        else:
            Display.unsupported_arg(display)
            Display.print_help(display)

    def list_tasks(self):
        try:
            line = self.read()
            if len(line) == 0:
                Display.no_todo(display)
                return
            max_length = self.max_length()
            Display.print_border(display, max_length)
            for i in range(len(line)):
                if argv[1] == "-lu" and line[i][0:3] == "[ ]":
                    Display.list_format(display, i, line)
                    Display.print_border(display, max_length)
                elif argv[1] == "-ld" and line[i][0:3] == "[x]":
                    Display.list_format(display, i, line)
                    Display.print_border(display, max_length)
                elif argv[1] == "-l":
                    Display.list_format(display, i, line)
                    Display.print_border(display, max_length)
        except TypeError:
            self.read()

    def max_length(self):
        line = self.read()
        max_length = 0
        for i in range(len(line)):
            if len(line[i]) > max_length:
                max_length = len(line[i])
        max_length = max_length + 6
        return max_length

    def new_task(self):
        try:
            tasks = open(self.name, "a")
            tasks.write("[ ] " + argv[2] + "\n")
            tasks.close()
        except IndexError:
            print("Unable to add: no task provided")

    def remove_task(self):
        try:
            del_line = argv[2]
            line = self.read()
            if int(argv[2]) > len(line):
                return print("Unable to remove: index is out of bound")
            del line[int(del_line) - 1]
            tasks = open(self.name, "w")
            for i in range(len(line)):
                tasks.write(line[i])
            tasks.close()
        except IndexError:
            return print("Unable to remove: no index provided")
        except ValueError:
            return print("Unable to remove: index is not a number")

    def complete_task(self):
        try:
            line = self.read()
            complete = int(argv[2]) - 1
            if int(argv[2]) > len(line):
                return print("Unable to check: index is out of bound")
            tasks = open(self.name, "w")
            for i in range(len(line)):
                if line[i][0:3] == "[ ]" and i == complete and argv[1] == "-c":
                    tasks.write("[x]" + line[i][3:])
                elif line[i][0:3] == "[x]" and i == complete and argv[1] == "-uc":
                    tasks.write("[ ]" + line[i][3:])
                else:
                    tasks.write(line[i])
            tasks.close()
        except IndexError:
            return print("Unable to check: no index provided")
        except ValueError:
            return print("Unable to check: index is not a number")

    def read(self):
        try:
            tasks = open(self.name, "r")
            line = tasks.readlines()
            tasks.close()
            return line
        except FileNotFoundError:
            tasks = open(self.name, "w")
            print("File didn't exist, now it is.")
            tasks.close()


class Display:

    def print_help(self):
        print("\n|================================|")
        print("| Command Line Todo Application  |\n|================================|\n \n  Command Line arguments:")
        print("  -l Lists all the tasks")
        print("  -lu Lists all the undone tasks")
        print("  -ld Lists all the done tasks")
        print("  -a Add a new task")
        print("  -r Removes a task")
        print("  -c Completes a task")
        print("  -uc Uncompletes a task")

    def no_todo(self):
        print("No todos for today! :)")

    def unsupported_arg(self):
        print("\nUnsupported argument")

    def list_format(self, i, line):
        print("| " + str(i + 1) + " - " + line[i], sep="", end="")

    def print_border(self, max_length):
        print("=" * max_length)


display = Display()
screen = Controller('todo.txt')
