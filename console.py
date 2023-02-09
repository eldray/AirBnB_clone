#!/usr/bin/python3
"""
AirBnb Clone Project CLI module - entry point of the command interpreter
"""

import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class defining the command interpreter"""

    prompt = "(hbnb) "
    classes_dict = {"BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "State": State}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Command for 'Ctrl+D'; Exits CLI
        """
        print()
        return True

    def emptyline(self):
        """
        Overwrites behaviour of emptyline + Enter
        - doesn't do anything
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes_dict.keys():
            print("** class doesn't exist **")
        else:
            instance = self.classes_dict[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in self.classes_dict.keys():
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                class_id = f"{args[0]}.{args[1]}"
                if class_id not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[class_id])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in self.classes_dict.keys():
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                class_id = f"{args[0]}.{args[1]}"
                if class_id not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[class_id]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        args = parse(line)
        new_list = []
        if len(line) == 0:
            for item in storage.all().values():
                new_list.append(item.__str__())
            print(new_list)
        else:
            if args[0] not in self.classes_dict.keys():
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if args[0] in key:
                        new_list.append(value.__str__())
                print(new_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in self.classes_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_id = f"{args[0]}.{args[1]}"
        if class_id in storage.all().keys():
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            elif len(args) == 4:
                setattr(storage.all()[class_id], args[2], args[3].strip('"'))
                storage.save()
        else:
            print("** no instance found **")


def parse(line):
    """ Method to parse line """
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()