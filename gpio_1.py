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
    b = SAKS.buzzer #蜂鸣器
    b.keep(1)
    alloff = list((False,) * 8)
    onone = [alloff[:] for i in range(8)]
    for i in range(8):
        onone[i][i] = True
    nums = {0:'1000', 1:'2000', 2:'0100', 3:'0200', 4:'0010', 5:'0020', 6:'0001', 7:'0002' }

    SAKS.ledrow.off()
    time.sleep(3)
    SAKS.ledrow.set_row([True, False, True, False, True, False, True, False])
    time.sleep(2)
    for i in range(8):
        SAKS.digital_display.show(nums[i])
        SAKS.ledrow.set_row(onone[i])
        time.sleep(0.5)
    SAKS.ledrow.off()

    SAKS.digital_display.show("2.3.3.3.")
 
try:
    init()
    while True:
        #00000001,00000010,00000100,00001000,00010000,00100000,01000000,10000000
        for i in [0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3F, 0x7F, 0xFF]:
            writeByte(i)
           time.sleep(0.1)
        #writeByte(0xff)
        #time.sleep(0.1)
        if __name__ == '__main__':
            main()
 
except KeyboardInterrupt:
    print("except")
    writeByte(0x00)
    GPIO.cleanup()
 
