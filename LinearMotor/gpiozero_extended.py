#code from https://thingsdaq.org/2022/03/01/h-bridge-and-dc-motor-with-raspberry-pi/

from gpiozero import DigitalOutputDevice, PWMOutputDevice


class Motor:
    times_run = 0
    def __init__(self, enable1=None, enable2=None, pwm1=None, pwm2=None):

        # Identifying motor driver type and assigning appropriate GPIO pins
        if pwm1 and pwm2:
            # Driver with 1 enable and 2 PWM inputs
            # Example: SN754410 quadruple half-H driver chip
            if not enable1:
                raise Exception('"enable1" pin is undefined.')
            self._dualpwm = True
            self._enable1 = DigitalOutputDevice(enable1)
            self._pwm1 = PWMOutputDevice(pwm1)
            self._pwm2 = PWMOutputDevice(pwm2)
        elif enable1 and enable2:
            # Driver with 2 enables and 1 PWM input
            # Example: L298 dual H-bridge motor speed controller board
            if not pwm1:
                raise Exception('"pwm1" pin is undefined.')
            self._dualpwm = False
            self._enable1 = DigitalOutputDevice(enable1)
            self._enable2 = DigitalOutputDevice(enable2)
            self._pwm1 = PWMOutputDevice(pwm1)
        else:
            raise Exception('Pin configuration is incorrect.')
        # Initializing output value
        self._value = 0

    def __del__(self):

        # Releasing GPIO pins
        if self._dualpwm:
            self._enable1.close()
            self._pwm1.close()
            self._pwm2.close()
        else:
            self._enable1.close()
            self._enable2.close()
            self._pwm1.close()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _):
        print('"value" is a read only attribute.')

    def set_output(self, output, brake=False):

        # Limiting output
        if output > 1:
            output = 1
        elif output < -1:
            output = -1
        # Forward rotation
        if output > 0:
            if self._dualpwm:
                self._enable1.on()
                self._pwm1.value = output
                self._pwm2.value = 0
            else:
                self._enable1.on()
                self._enable2.off()
                self._pwm1.value = output
        # Backward rotation
        elif output < 0:
            if self._dualpwm:
                self._enable1.on()
                self._pwm1.value = 0
                self._pwm2.value = -output
            else:
                self._enable1.off()
                self._enable2.on()
                self._pwm1.value = -output
        # Stop motor
        elif output == 0:
            if brake:
                if self._dualpwm:
                    self._enable1.off()
                    self._pwm1.value = 0
                    self._pwm2.value = 0
                else:
                    self._enable1.off()
                    self._enable2.off()
                    self._pwm1.value = 0
            else:
                if self._dualpwm:
                    self._enable1.on()
                    self._pwm1.value = 0
                    self._pwm2.value = 0
                else:
                    self._enable1.on()
                    self._enable2.on()
                    self._pwm1.value = 0

        # Updating output value property
        self._value = output

        