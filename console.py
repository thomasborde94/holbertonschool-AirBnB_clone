#!/usr/bin/python3
"""Console for AirBnB"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

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
        """create a new instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            newInstance = eval(arg)()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, arg):
        token = arg.split(" ")
        dict_obj = storage.all()

        if len(arg) == 0:
            print("** class name missing **")

        elif token[0] not in self.class_list:
            print("** class doesn't exist **")

        elif len(token) < 2:
                print("** instance id missing **")

        else:
            instance_key = "{}.{}".format(token[0], token[1])
            
            if instance_key not in dict_obj.keys():
                print("** no instance found **")

            else:
                print(dict_obj[instance_key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
