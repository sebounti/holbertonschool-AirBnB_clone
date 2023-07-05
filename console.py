#!/usr/bin/python3
"""
command module
"""

import cmd, sys


class HBNBCommand(cmd.Cmd):
        prompt = "(hbnb) "
        
        def do_quit(self, arg):
                "Quit command to exit the program"
                return True
        
        def do_EOF(self, arg):
                "End-of-file : a code, maker, or signal used to indicate the end of a file of data"
                return True
                
        def do_help(self, arg):
                "help command if you need help"
                return super().do_help(arg)
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()