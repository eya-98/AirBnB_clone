#!/usr/bin/python3
"""Holberton Module"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """define HBNBCOMMand as a class"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """implement EOF method"""
        return True

    def do_quit(self, args):
        """implement quit"""
        return True

    def emptyline(self):
        """implement empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
