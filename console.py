#!/usr/bin/python3
"""this model is for defining the console
and it commands
"""
import cmd

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
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
    
    def do_create(self, name):
        if name:
            if name in calsses.keys():
                new = classes[name]()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_show(self, name):
        args = name.split()
        """
        print string representation of an instance
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        ob = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in ob:
            print(str(ob[key]))
        else:
            print("** no instance found **")
            
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
