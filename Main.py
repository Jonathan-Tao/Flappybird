from pynput.keyboard import Key, Controller
import time
import keyboard

x = True

keyboard = Controller()

keyboard.press(Key.space)
keyboard.release(Key.space)

#while x == True:

#    time.sleep(1)
#    for char in "sin":
#        keyboard.press(char)
#        keyboard.release(char)
#        
#    keyboard.press(Key.enter)
#    keyboard.release(Key.enter)
