from pynput import keyboard  
from pynput.keyboard import Listener

def keyPress(key):
    pass

def keyReleased(key):
    pass
    
with Listener(keyPress = keyPress, keyReleased = keyReleased) as listener:
    listener.join()