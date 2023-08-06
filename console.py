#!/usr/bin/python3
"""class console interactive"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")
    def do_destroy(self, arg):
        """Deletes an instance based on the class"""

        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")
    def do_all(self, arg):
        """Prints all string representation of all instances"""

        if not arg:
            for obj in all_objs.values():
                print(obj)
                return
        try:
            eval(arg)
        except:
            print("** class doesn't exist **")
            return
        for obj in all_objs.values():
            if type(obj).__name__ == arg:
                print(obj)


    def do_update(self, arg):
        """Updates an instance based on the class"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
