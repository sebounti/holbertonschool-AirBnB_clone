#!/usr/bin/python3
"""
command module
"""

import cmd
import sys
import json
from models.base_model import BaseModel


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
            class_name = arg.split[0]
            instance = eval(class_name)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")
        
    def do_show(self, arg):
        """show a represantation of an instance based 
        on is name class and id

        Args:
            arg (str): argument after the command
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        if len(args) < 2 or len(args) == 0:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        
        try:
            instance = eval(class_name).get(instance_id)
            if instance:
                print(instance)
            else:
                print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id

        Args:
            arg (str): argument after the command
        """
        if not arg:
                print("** class name missing **")
                return
            
        args = arg.split()

        if len(args) < 2 or len(args) == 0:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        
        try:
            instance = eval(class_name).get(instance_id)
            if instance:
                instance.delete()
            else:
                print("** instance id missing **")
            storage.save()
        except NameError:
            print("** class doesn't exist **")
        
    def do_all(self, arg):
        """Prints all string representation of all instances based

        Args:
            arg (str): argument after the command
        """
        if not arg:
            instance = storage.all().values()
        else:
            try:
                class_name = eval(arg).__name__
                instance = [instance for instance in storage.all().values() if instance.__class__.__name__ == class_name]
            except NameError:
                print("** class doesn't exist **")
        print([str(instance) for instance in instance])
        
    def do_update(self, arg):
        """ Updates an instance based on the class name and id 

        Args:
            arg (str): argument after the command
        """
        if not arg:
            print("** class name missing **")
        
        args = arg.split()
        if len(args) < 2 or len(args) == 0:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        
        try:
            instance = eval(class_name).get(instance_id)
            if instance is None:
                print("** no instance found **")
                
            if len(args) < 3:
                print("** attribute name missing **")
                return
            
            attribute_name = args[2]
            
            if len(args) < 4:
                print("** value missing **")
            
            attribute_value = args[3]
            
            setattr(instance, instance, type(getattr(instance, attribute_name))(attribute_value))
            instance.save()
            
        except NameError:
            print("** class doesn't exist **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
