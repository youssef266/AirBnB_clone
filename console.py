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
    prompt = '(hbnb) '
    
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
    

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
            if name in HBNBCommand.classes.keys():
                new = HBNBCommand.classes[name]()
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
        if args[0] not in HBNBCommand.classes.keys():
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

    def do_destroy(self, name):
        """
        Delete an instance based on the class name and ID also changes are saved to the JSON file.
        """
        args = name.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        ob = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in ob:
            del ob[key]
            storage.save()
        else:
            print("** no instance found **")
    def do_all(self, arg):
        """Prints all string representations of instances based on the class name.
        
        Usage: all [ClassName]
        If ClassName is not provided, it prints all instances of the default class (BaseModel).
        """
        arg_l = arg.split()
        if len(arg_l) > 0 and arg_l[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj_l = []
            for obj in storage.all().values():
                if len(arg_l) > 0 and arg_l[0] == obj.__class__.__name__:
                    obj_l.append(obj.__str__())
                elif len(arg_l) == 0:
                    obj_l.append(obj.__str__())
            print(obj_l)
    
    def do_update(self, arg):
        """ """
        arg_l = arg.split()
        obj_dict = storage.all()

        if len(arg_l) == 0:
            print("** class name missing **")
            return False
        if arg_l[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_l) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_l[0], arg_l[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_l) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_l) == 3:
            try:
                type(eval(arg_l[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_l) == 4:
            obj = obj_dict["{}.{}".format(arg_l[0], arg_l[1])]
            if arg_l[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_l[2]])
                obj.__dict__[arg_l[2]] = valtype(arg_l[3])
            else:
                obj.__dict__[arg_l[2]] = arg_l[3]
        elif type(eval(arg_l[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_l[0], arg_l[1])]
            for k, v in eval(arg_l[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_l = arg.split()
        counter = 0
        for obj in storage.all().values():
            if arg_l[0] == obj.__class__.__name__:
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
