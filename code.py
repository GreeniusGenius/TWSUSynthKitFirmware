#Adafruit Circuit Python
import time
import random
import usb_midi
import adafruit_midi
import digitalio
import analogio
import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
import asyncio
import countio
import board

blebtn = digitalio.DigitalInOut(board.GP20) #set the pin as wired on pcb
blebtn.switch_to_input(pull=digitalio.Pull.UP) #pull the pin up so signal isn't floating

# Use default HID descriptor
midi_service = adafruit_ble_midi.MIDIService() #initialise midiservice class
advertisement = ProvideServicesAdvertisement(midi_service) #advertise bluetooth child device
# advertisement.appearance = 961

def blerst():
    try:
        ble = adafruit_ble.BLERadio()
        if ble.connected:
            for c in ble.connections:
                c.disconnect()
    except Error as e:
        print(e)

def getSound(io):
    return (io * 3.3) / 16384 #midi library is 14 bit but adc is converted to 16 bit by library

try:
    midi = adafruit_midi.MIDI(midi_out=(usb_midi.ports[1], midi_service), out_channel=0)
except Error as e:
    print(e)

try:
    ble = adafruit_ble.BLERadio()
    soundADC = analogio.AnalogIn(board.ADC0)
    adafruit_midi.start(midi)
    adafruit_midi.note_on(note=12) #just set a default note
except Exception as e:
    print(e)



while True:
    try:
        if not blebtn.value:
            blerst() #check if bluetooth pairing button pressed
        else:
            pass
        io = soundADC.value
        sound = getSound(io) #call the function
        adafruit_midi.pitch_bend.PitchBend(sound)
        adafruit_midi.midi_continue
        ble.start_advertising(advertisement)
    except Exception as e:
        print(e)
