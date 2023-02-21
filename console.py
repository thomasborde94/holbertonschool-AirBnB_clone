#!/usr/bin/python3
"""Console for AirBnB"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class of the interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """quits the console"""
        exit()
    def do_EOF(self, arg):
        """quits the console"""
        print()
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
