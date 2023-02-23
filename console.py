#!/usr/bin/python3
"""Console for AirBnB"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class of the interpreter"""
    prompt = '(hbnb)'
    class_list = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """quits the console"""
        exit()

    def do_EOF(self, arg):
        """quits the console using ctrl+D"""
        print()
        exit()

    def emptyline(self):
        """handles empty lines"""
        pass

    def do_create(self, arg):
        """create a new instance of a class un class_list"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            newInstance = eval(arg)()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, arg):
        """prints the string representation of an instance"""
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

    def do_destroy(self, arg):
        """Deletes an instances of a class"""
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
                del dict_obj[instance_key]
                storage.save()

    def do_all(self, arg):
        """prints string representation of all instances in __objects"""
        dict_obj = storage.all()
        list_obj = []

        if len(arg) == 0:
            for keys, values in dict_obj.items():
                list_obj.append(str(values))
            print(list_obj)

        elif arg in self.class_list:
            for keys, values in dict_obj.items():
                if values.__class__.__name__ == arg:
                    list_obj.append(str(values))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance of a class by adding or updating attribute"""
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

            elif len(token) < 3:
                print("** attribute name missing **")

            elif len(token) < 4:
                print("** value missing **")

            else:
                setattr(dict_obj[instance_key], token[2], token[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
