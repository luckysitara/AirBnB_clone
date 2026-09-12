#!/usr/bin/python3
'''
import all modules needed
'''
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City


def parse(line):
    '''
    Helper to parse arguments respecting double quotes
    '''
    try:
        return shlex.split(line)
    except Exception:
        return line.split()


'''
create a class called the HBNBCommand
'''


class HBNBCommand(cmd.Cmd):

    '''
HBNB Console for the win
    '''
    prompt = "(hbnb) "
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, args):
        '''Create a new instance of BaseModel, save it and prints the id
           Usage: create <class name>
        '''
        arg_list = parse(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_creation = eval(arg_list[0] + '()')
            models.storage.save()
            print(new_creation.id)

    def do_show(self, args):
        '''Prints the string representation of a specific instance
           Usage: show <class name> <id>
        '''
        arg_list = parse(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key_value = arg_list[0] + '.' + arg_list[1]
            if key_value in objects:
                print(objects[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        '''Delete an instance
           Usage: destroy <class name> <id>
        '''
        arg_list = parse(args)
        objects = models.storage.all()

        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print('** instance id missing **')
        else:
            key_find = arg_list[0] + '.' + arg_list[1]
            if key_find in objects:
                del objects[key_find]
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''Print a string representation of all instances
           Usage: all <class name>
        '''
        arg_list = parse(args)
        objects = models.storage.all()
        new_list = []

        if len(arg_list) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == arg_list[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        '''update an instance
           Usage update <class name> <id> <attribute name> "<attribute value>"
        '''
        arg_list = parse(args)

        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        key_find = arg_list[0] + '.' + arg_list[1]
        if key_find not in objects:
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return

        obj = objects[key_find]
        attr_name = arg_list[2]
        attr_val = arg_list[3]

        if attr_name in ["id", "created_at", "updated_at"]:
            return

        if hasattr(obj, attr_name) and type(
                getattr(obj, attr_name)) is not type(None):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_val = attr_type(attr_val)
            except (ValueError, TypeError):
                pass
        else:
            try:
                attr_val = int(attr_val)
            except ValueError:
                try:
                    attr_val = float(attr_val)
                except ValueError:
                    pass

        setattr(obj, attr_name, attr_val)
        obj.save()

    def do_quit(self, arg):
        '''
quit to end the programe
    '''
        return True

    def do_EOF(self, arg):
        '''
handle end of file and quit like a pro
        '''
        return True

    def emptyline(self):
        '''
do something if user type
else do nothing
and follow dry principle
        '''
        pass

    def default(self, line):
        """ Called for unknow command syntax """
        if "." in line:
            cmd_args = line.split(".")
            if cmd_args[0] in self.__classes:
                if cmd_args[1] == "count()":
                    instances = [v for k, v in models.storage.all().items()
                                 if k.startswith(cmd_args[0])]
                    print(len(instances))
                elif cmd_args[1].startswith("show"):
                    inst_id = cmd_args[1].split('"')[1]
                    self.do_show("{} {}".format(cmd_args[0], inst_id))
                elif cmd_args[1].startswith("destroy"):
                    inst_id = cmd_args[1].split('"')[1]
                    self.do_destroy("{} {}".format(cmd_args[0], inst_id))
        else:
            print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
