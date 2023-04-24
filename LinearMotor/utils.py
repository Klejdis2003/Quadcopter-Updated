#Code from https://thingsdaq.org/2022/03/01/h-bridge-and-dc-motor-with-raspberry-pi/ with modifications to fit our needs

# Importing modules and classes
import time
import numpy as np
import LinearMotor.gpiozero_extended
import RPi.GPIO as GPIO

class Motor:
    
    mymotor = LinearMotor.gpiozero_extended.Motor(enable1=6, pwm1=5, pwm2=13)
    def move(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.OUT)
        mymotor = self.mymotor
        
        # Assigning parameter values
        T = 4  # Period of sine wave (s)
        u0 = 1  # Motor output amplitude
        tstop = 2 # Sine wave duration (s)
        tsample = 0.01  # Sampling period for code execution (s)

        # Creating motor object using GPIO pins 16, 17, and 18
        # (using SN754410 quadruple half-H driver chip)
        

        # Initializing current time stamp and starting clock
        tprev = 0
        tcurr = 0
        tstart = time.perf_counter()
        while tcurr <= tstop:
            # Getting current time (s)
            tcurr = time.perf_counter() - tstart
            # Doing I/O every `tsample` seconds
            if (np.floor(tcurr/tsample) - np.floor(tprev/tsample)) == 0:
                # Assigning motor sinusoidal output using the current time stamp
                sin_wave = u0 * np.sin((2*np.pi/T) * tcurr) #using slightly modified SHM equation to control the motor
                if mymotor.times_run % 2 == 0:
                    mymotor.set_output(np.abs(sin_wave)) #closes the claw
                else:
                    mymotor.set_output(-np.abs(sin_wave)) #opens the claw

            tprev = tcurr # Updating previous time value
        print('Claw moved.')
        mymotor.set_output(0, brake=True) #stop the motor
        self.mymotor.times_run += 1
        
        del mymotor
    
    def close(self):
        mymotor = self.mymotor

         # Assigning parameter values
        T = 4  # Period of sine wave (s)
        u0 = 1  # Motor output amplitude
        tstop = 2 # Sine wave duration (s)
        tsample = 0.01  # Sampling period for code execution (s)

        # Creating motor object using GPIO pins 16, 17, and 18
        # (using SN754410 quadruple half-H driver chip)
        

        # Initializing current time stamp and starting clock
        tprev = 0
        tcurr = 0
        tstart = time.perf_counter()
        while tcurr <= tstop:
            # Getting current time (s)
            tcurr = time.perf_counter() - tstart
            # Doing I/O every `tsample` seconds
            if (np.floor(tcurr/tsample) - np.floor(tprev/tsample)) == 0:
                # Assigning motor sinusoidal output using the current time stamp
                sin_wave = u0 * np.sin((2*np.pi/T) * tcurr)
                mymotor.set_output(np.abs(sin_wave))
            # Updating previous time value
            tprev = tcurr
        mymotor.set_output(0, brake=True)
        self.mymotor.times_run += 1
        print('Motor back to original, closed position.')
        del mymotor



