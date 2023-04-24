import RPi.GPIO as GPIO
from numpy import sin, abs
import time

class Continous_Servo:
    pin = 16
    rot_time = 8
    held = False
    cw_pressed = 0 #counts how many time the rotate_cw is called. This way, I can determine if it should start/stop.
    ccw_pressed = 0 #counts how many time the rotate_ccw is called. This way, I can determine if it should start/stop
    def setGPIO(self):
        GPIO.setwarnings(False)   
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
    
    def rotate_cw(self):
        if self.cw_pressed % 2 == 0:
            self.setGPIO()
            p = GPIO.PWM(self.pin, 100)
            p.start(11)
        else:
            p.stop()
            GPIO.cleanup() 
        cw_pressed += 1

    def rotate_ccw(self):
        if self.ccw_pressed % 2 == 0:
            self.setGPIO()
            p = GPIO.PWM(self.pin, 100)
            p.start(20)
        else:
            p.stop()
            GPIO.cleanup() 
        ccw_pressed += 1
    
