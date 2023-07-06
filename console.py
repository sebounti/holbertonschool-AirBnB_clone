#!/usr/bin/python3
"""
command module
"""

import cmd
import sys
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End-of-file : used to indicate the end of a file of data"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel

        Args:
            arg (str): _first argument after the command
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = arg.split()[0]
            instance = eval(class_name)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show a representation of an instance based on its class name and ID"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            instances = storage.all()
            for instance in instances.values():
                if instance.__class__.__name__ == class_name and instance.id == instance_id:
                    print(instance)
                    return
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            instances = storage.all()
            for key, instance in instances.items():
                if instance.__class__.__name__ == class_name and instance.id == instance_id:
                    del instances[key]
                    storage.save()
                    return
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representation of all instances based on the class name"""
        if not arg:
            instances = storage.all().values()
        else:
            try:
                class_name = eval(arg).__name__
                instances = [instance for instance in storage.all().values() if instance.__class__.__name__ == class_name]
            except NameError:
                print("** class doesn't exist **")
                return

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            instance_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        instances = storage.all()
        instance = None
        for obj in instances.values():
            if obj.__class__.__name__ == class_name and obj.id == instance_id:
                instance = obj
                break

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]

        setattr(instance, attr_name, type(getattr(instance, attr_name))(attr_value))
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
