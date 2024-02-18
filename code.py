print("kmk")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.midi import MidiKeys


keyboard = KMKKeyboard()
keyboard.modules.append(MidiKeys())

keyboard.col_pins = (board.GP6,board.GP7,)
keyboard.row_pins = (board.GP8,board.GP9,)


#  |6|7|
# -|-|-|
# 8|a|b|
# 9|c|d|
# test here: 
keyboard.diode_orientation = DiodeOrientation.COL2ROW
velo = 64

keyboard.keymap = [
    [KC.MIDI_NOTE(60, velo),KC.MIDI_NOTE(62, velo),
     KC.MIDI_NOTE(64, velo),KC.MIDI_NOTE(65, velo),]
]

if __name__ == '__main__':
    keyboard.go()
