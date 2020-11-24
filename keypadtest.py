from pad4pi import rpi_gpio
import time
count =0
KEYPAD = [
    ["1", "2"," 3"],
    ["4", "5", "6"],
    ["7","8","9"],
    ["*", "0", "#"]
]

ROW_PINS = [18,23,24,25] # BCM numbering
COL_PINS = [10, 9, 11] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
    print(key)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)


    
