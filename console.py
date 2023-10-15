#!/usr/bin/python3
'''
import all modules needed
'''
import cmd

'''
create a class called the HBNBCommand
'''


class HBNBCommand(cmd.Cmd):

    '''
HBNB Console for the win
    '''

    prompt = '(hbnb)'

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
