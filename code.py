print("kmk")
import board
import time
import pulseio # for piezo buzzer

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

# ************removing encoder for now*******************
# encoder_handler.pins = (
#     # regular direction encoder and a button
#     (board.GP14, board.GP15, board.GP13,), # encoder #1 
#     )

# *********** pin init **********************************
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,)
keyboard.col_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


#	layout2	F3 to B5	melodica	
#		9	10	11	12	13	14	15	
#									
#	0				F#	G#	A#		
#	1	C6*			F	G	A	B	
#	2	C#	D#		F#	G#	A#		
#	3	C4	D	E	F	G	A	B	
#	4	C#	D#		F#	G#	A#		
#	5	C5	D	E	F	G	A	B	
#									
# *might or might not add

#  |6|7|
# -|-|-|
# 8|a|b|
# 9|c|d|
# test here: 

# ******** frequencies for the piezo buzzer ***************
notes = {
    'C4': 261.63,
    'C#4': 277.18,
    'D4': 293.66,
    'D#4': 311.13,
    'E4': 329.63,
    'F4': 349.23,
    'F#4': 369.99,
    'G4': 392.00,
    'G#4': 415.30,
    'A4': 440.00,
    'A#4': 466.16,
    'B4': 493.88
}
# Set up the buzzer PWM output
buzzer = pulseio.PWMOut(board.D16, duty_cycle=0, frequency=440, variable_frequency=True)



def testprint(key, keyboard, *args):
    print("ee")

velo = 80
octave = 60 # C4/Middle C - add or minus to get note
# KC.NO, = disabled key 
keyboard.keymap = [9
    [KC.NO,                  KC.NO,                  KC.NO,					 KC.MIDI_NOTE(octave - 6, velo), KC.MIDI_NOTE(octave - 4, velo), KC.MIDI_NOTE(octave - 2, velo), KC.NO,
     KC.NO,                  KC.NO,                  KC.NO,                  KC.MIDI_NOTE(octave - 7, velo), KC.MIDI_NOTE(octave - 5, velo), KC.MIDI_NOTE(octave - 3, velo), KC.MIDI_NOTE(octave - 1, velo),
     KC.MIDI_NOTE(octave + 1, velo), KC.MIDI_NOTE(octave + 3, velo), KC.NO,					 KC.MIDI_NOTE(octave + 6, velo), KC.MIDI_NOTE(octave + 8, velo), KC.MIDI_NOTE(octave + 10, velo), KC.NO,
     KC.MIDI_NOTE(octave, velo), KC.MIDI_NOTE(octave + 2, velo), KC.MIDI_NOTE(octave + 4, velo), KC.MIDI_NOTE(octave + 5, velo), KC.MIDI_NOTE(octave + 7, velo), KC.MIDI_NOTE(octave + 9, velo), KC.MIDI_NOTE(octave + 11, velo),
     KC.MIDI_NOTE(octave + 13, velo), KC.MIDI_NOTE(octave + 15, velo), KC.NO,					 KC.MIDI_NOTE(octave + 18, velo), KC.MIDI_NOTE(octave + 20, velo), KC.MIDI_NOTE(octave + 22, velo), KC.NO,
     KC.MIDI_NOTE(octave + 12, velo), KC.MIDI_NOTE(octave + 14, velo), KC.MIDI_NOTE(octave + 16, velo), KC.MIDI_NOTE(octave + 17, velo), KC.MIDI_NOTE(octave + 19, velo), KC.MIDI_NOTE(octave + 21, velo), KC.MIDI_NOTE(octave + 22, velo),
     ],
    [
        
    ]
]

# BENDDOWN = KC.NO
# BENDUP = KC.NO
# encoder_handler.map = [ (( BENDDOWN, BENDUP, KC.MIDI_NOTE(60, velo)),)] # Layer 1
# BENDDOWN.after_press_handler(testprint)
# BENDUP.after_press_handler(testprint)

if __name__ == '__main__':
    keyboard.go()
