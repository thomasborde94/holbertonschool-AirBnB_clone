#!/usr/bin/python3
"""Console for AirBnB"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """class of the interpreter"""
    prompt = '(hbnb)'
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """quits the console"""
        exit()
    def do_EOF(self, arg):
        """quits the console"""
        print()
        exit()

    def emptyline(self):
        """handles empty lines"""
        pass

    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            newInstance = eval(arg)()
            newInstance.save()
            print(newInstance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
