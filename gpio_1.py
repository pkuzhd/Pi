#The first GPIO file
import RPi.GPIO as GPIO
import time
from sakshat import SAKSHAT 
GPIO.setmode(GPIO.BCM)
 
DS = 6
SHCP = 19
STCP = 13
 
def init():
    GPIO.setup(DS, GPIO.OUT)
    GPIO.setup(SHCP, GPIO.OUT)
    GPIO.setup(STCP, GPIO.OUT)
 
    GPIO.output(DS, GPIO.LOW)
    GPIO.output(SHCP, GPIO.LOW)
    GPIO.output(STCP, GPIO.LOW)
 
def writeBit(data):
    GPIO.output(DS, data)
 
    GPIO.output(SHCP, GPIO.LOW)
    GPIO.output(SHCP, GPIO.HIGH)
 
def writeByte(data):
    for i in range (0, 8):
        writeBit((data >> i) & 0x01)
    GPIO.output(STCP, GPIO.LOW)
    GPIO.output(STCP, GPIO.HIGH)

def main():
    b = SAKS.buzzer #feng ming qi
    b.keep(1)
    alloff = list((
 
try:
    init()
    while True:
        #00000001,00000010,00000100,00001000,00010000,00100000,01000000,10000000
        for i in [0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3F, 0x7F, 0xFF]:
            writeByte(i)
           time.sleep(0.1)
        #writeByte(0xff)
        #time.sleep(0.1)
 
except KeyboardInterrupt:
    print("except")
    writeByte(0x00)
    GPIO.cleanup()
