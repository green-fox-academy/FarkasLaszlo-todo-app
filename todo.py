from sys import argv


class Controller:
    def __init__(self, name):
        self.name = name
        if len(argv) == 1:
            self.print_usage()
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
        else:
            print("\nUnsupported argument")
            self.print_usage()

    def print_usage(self):
        print("\n|===============================|")
        print("| Command Line Todo Application |\n""|===============================|\n \n""  Command Line arguments:")
        print("  -l Lists all the tasks")
        print("  -lu Lists all the undone tasks")
        print("  -ld Lists all the done tasks")
        print("  -a Add a new task")
        print("  -r Removes a task")
        print("  -c Completes a task")

    def list_tasks(self):
        tasks = open(self.name, "r")
        line = tasks.readlines()
        if len(line) == 0:
            print("No todos for today! :)")
        for i in range(len(line)):
            if argv[1] == "-lu" and line[i][0:3] == "[ ]":
                print(str(i + 1) + " - " + line[i], sep="", end="")
            elif argv[1] == "-ld" and line[i][0:3] == "[x]":
                print(str(i + 1) + " - " + line[i], sep="", end="")
            elif argv[1] == "-l":
                print(str(i + 1) + " - " + line[i], sep="", end="")
        tasks.close()

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
            tasks = open(self.name, "r")
            line = tasks.readlines()
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
            tasks = open(self.name, "r")
            line = tasks.readlines()
            complete = int(argv[2]) - 1
            tasks.close()
            if int(argv[2]) > len(line):
                return print("Unable to check: index is out of bound")
            tasks = open(self.name, "w")
            for i in range(len(line)):
                if line[i][0:3] == "[ ]" and i == complete:
                    tasks.write("[x]" + line[i][3:])
                else:
                    tasks.write(line[i])
            tasks.close()
        except IndexError:
            return print("Unable to check: no index provided")
        except ValueError:
            return print("Unable to check: index is not a number")


screen = Controller('todo.txt')
