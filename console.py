import cmd


class HBNBCommad(cmd.cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ commad to exit the program """

        return True

    def do_EOF(self, arg):
        """ funtion command to exit the program"""

        return True
    
    def emptyline(self):
        """line + enter execute anything"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
