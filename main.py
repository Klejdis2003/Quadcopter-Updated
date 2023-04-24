#created for backup if the vnc server does not work well during the challenge

from time import *
from cameracontrols import Servo
from LinearMotor.utils import Motor
from contnious_servo import Continous_Servo
from picamera import CameraFunctions

servo = Servo() #camera servo
cont_servo = Continous_Servo() #rotational motor
my_motor = Motor() #linear motor
cf = CameraFunctions #static functions

while True:
    print(
    '''
    Commands:
    0 -- Tilt
    1 -- Rotate Clockwise
    2 -- Rotate CounterClockwise
    3 -- Take Picutre
    4 -- Record Video
    ''')

    commands = {
                '0': servo.tilt, 
                '1': cont_servo.rotate_cw, 
                '2':cont_servo.rotate_ccw, 
                '3': cf.picture,
                '4': cf.video
                }

    command = input("Enter your command: ")
    commands[command]()