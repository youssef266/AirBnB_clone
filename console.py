#!/usr/bin/python3
"""this model is for defining the console
and it commands
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """It is Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """it's the Exit the program when EOF is encountered"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """an command for Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
