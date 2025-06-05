#Adafruit Circuit Python
import time
import random
import usb_midi
import adafruit_midi
import digitalio
import analogio

try:
    midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)
except Error as e:
    print(e)

soundADC = analogio.AnalogIn(board.ADC0)
adafruit_midi.start(midi)
adafruit_midi.note_on(note=12)

def getSound(io):
    return (io * 3.3) / 16384
while True:
    io = soundADC.value
    sound = getSound(io)
    adafruit_midi.pitch_bend.PitchBend(sound)
    adafruit_midi.midi_continue


