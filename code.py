print("kmk")
import board
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.midi import MidiKeys
from kmk.modules.encoder import EncoderHandler
import adafruit_midi

timenow = time.monotonic()
print(f"time is: {timenow}")
keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.modules.append(MidiKeys())

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP14, board.GP15, board.GP13,), # encoder #1 
    )

keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3,)
keyboard.col_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#									
#		4	5	6	7	8	9	10	
#									
#	0	C#	D#		F#	G#	A#		
#	1	C	D	E	F	G	A	B	
#	2	C#	D#		F#	G#	A#		
#	3	C	D	E	F	G	A	B	
#									

#  |6|7|
# -|-|-|
# 8|a|b|
# 9|c|d|
# test here: 


def testprint(key, keyboard, *args):
    print("ee")

velo = 80
# KC.NO, = disabled key 
keyboard.keymap = [
    [KC.MIDI_NOTE(61, velo), KC.MIDI_NOTE(63, velo), KC.NO,					 KC.MIDI_NOTE(66, velo), KC.MIDI_NOTE(68, velo), KC.MIDI_NOTE(70, velo), KC.NO,
     KC.MIDI_NOTE(60, velo), KC.MIDI_NOTE(62, velo), KC.MIDI_NOTE(64, velo), KC.MIDI_NOTE(65, velo), KC.MIDI_NOTE(67, velo), KC.MIDI_NOTE(69, velo), KC.MIDI_NOTE(71, velo),
     KC.MIDI_NOTE(73, velo), KC.MIDI_NOTE(75, velo), KC.NO,					 KC.MIDI_NOTE(78, velo), KC.MIDI_NOTE(80, velo), KC.MIDI_NOTE(82, velo), KC.NO,
     KC.MIDI_NOTE(72, velo), KC.MIDI_NOTE(74, velo), KC.MIDI_NOTE(76, velo), KC.MIDI_NOTE(77, velo), KC.MIDI_NOTE(79, velo), KC.MIDI_NOTE(81, velo), KC.MIDI_NOTE(82, velo),
     ]
]

BENDDOWN = KC.NO
BENDUP = KC.NO
encoder_handler.map = [ (( BENDDOWN, BENDUP, KC.MIDI_NOTE(60, velo)),)] # Layer 1
BENDDOWN.after_press_handler(testprint)
BENDUP.after_press_handler(testprint)

if __name__ == '__main__':
    keyboard.go()
