#!usr/bin/python3
"""Holberton Module"""


class HBNBCommand(cmd.Cmd):
    """define HBNBCOMMand as a class"""
     def do_EOF(self, line):
         """implement EOF method"""
         return True

    def close(self):
        """implement quit method"""

        if self.file:
            self.file.close()
            self.file = None
