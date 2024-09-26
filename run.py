import keyboard
import pyperclip

from setArea import set_area
from readArea import read_area

def save_clipboard():
    text = read_area()
    pyperclip.copy(text)

# Printing instructions
print("Press '1' to set area.\nPress '2' to save content to clipboard.\nPress 'esc' to exit.")
    
while True:
    if keyboard.is_pressed('1'):
        set_area()
    
    if keyboard.is_pressed('2'):
        save_clipboard()    
    
    if keyboard.is_pressed('esc'):
        break