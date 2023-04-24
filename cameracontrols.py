import RPi.GPIO as GPIO
import time
class Servo:
    pin = 12
    pan_called = 0

    def setGPIO(self):
        GPIO.setwarnings(False)   
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        p = GPIO.PWM(self.pin, 100) # GPIO 12 for PWM with 50Hz
        p.start(2.5) # Initialization
        return p

    def tilt(self):
        p = self.setGPIO()

        if self.pan_called % 2 == 0:
            dutycycle = 2.5
            difference = 1
        else:
            dutycycle = 32.5
            difference = -1

        while True:
            time.sleep(0.01)
            dutycycle += difference
            p.ChangeDutyCycle(dutycycle)
            if dutycycle == 32.5 or dutycycle == 0.5:
                break
        self.pan_called += 1
        p.stop()
        GPIO.cleanup()
        
