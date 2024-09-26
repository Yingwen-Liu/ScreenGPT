import keyboard
import pyperclip

from setArea import set_area
from readArea import read_area

def save_clipboard():
    text = read_area()
    pyperclip.copy(text)

# Printing instructions
print("Press 'up' to set area.\nPress 'down' to save content to clipboard.\nPress 'esc' to exit.")
    
while True: 
    if keyboard.is_pressed('up'):
        set_area()
    
    if keyboard.is_pressed('down'):
        save_clipboard()    
    
    if keyboard.is_pressed('esc'):
        break