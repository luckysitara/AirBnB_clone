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

    def do_quit(self):
        '''
        quit to end the programe
        '''
        pass

    def do_EOF(self):
        '''
        handle end of file and quit like a pro
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
