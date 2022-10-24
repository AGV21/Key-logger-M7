from pynput.keyboard import Key
from pynput.keyboard import Listener 
 
keys = []

def functionPressed(key):
    keys.pressed(key)
    key.file(keys)
    

