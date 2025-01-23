import sys
import socket
import os


Tlist = []
Mlist = []

def Home():
    global Tlist
    global Mlist
    while True:
        Tlist_str = "\n".join(Tlist)
        Mlist_str = "\n".join(Mlist)
        print('T\n' + Tlist_str + '\nM\n' + Mlist_str)
        msg = input('add = /add\ncheck = num\n\n\n')
        if msg == '/add':
            todoname = input('Todo name plz:')
            TorM = input('T or M?:')
            if TorM == 'T' or TorM == 't':
                Tlist.append(todoname)
            if TorM == 'M' or TorM == 'm':
                Mlist.append(todoname)
            else:
                print('Not')


Home()
