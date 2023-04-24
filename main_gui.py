from tkinter import *
from time import *
from cameracontrols import Servo
from LinearMotor.utils import Motor
from contnious_servo import Continous_Servo
from picamera import CameraFunctions


servo = Servo() #camera servo
cont_servo = Continous_Servo() #rotational servo
my_motor = Motor() #linear motor
cf = CameraFunctions 

class Btn:
    buttons = []
    def __init__(self, row = 0, column = 0):
        self.row = row
        self.column = column

    def createButton(self, text = "blank", color="gray", command = ""): #simplifying button creation
        w = root.winfo_width()
        h = root.winfo_height()
        btn = Button(root, text = text, command = command, bg = color, height = h, width = w) 
        btn.pack()
        self.buttons.append(btn)
        return btn
    def update(self):
        w = root.winfo_width()
        h = root.winfo_height()
        for btn in self.buttons:
            btn.configure(width = w, height = h//(25*n_buttons))
            btn.pack()

def close(): #to be called when the app is terminated
    my_motor.close() #retracts the claw to opening position
    print('App terminated.')
    root.quit()
    
    

global root
root = Tk()
root.geometry('1920x1080')
root.minsize(width = 500, height = 500)
 


btn = Btn()

#creating all buttons
cameraservo_btn = btn.createButton("Tilt", "red", Servo().tilt)
actuator_btn = btn.createButton(text = "Move Linear Motor", color = 'green', command = my_motor.move)
cw_btn = btn.createButton(text = "Rotate Clockwise", color = 'yellow', command = cont_servo.rotate_cw )
ccw_btn = btn.createButton(text = 'Rotate CounterClockwise', color = 'orange', command = cont_servo.rotate_ccw )
camerapicture_btn = btn.createButton(text = "Take Picture", color = 'purple', command = cf.picture)
cameravideo_btn = btn.createButton(text = "Record Video", color = 'pink', command = lambda: cf.video(5))

global n_buttons
n_buttons = len(btn.buttons) #imortant when calculating the height of each button in the update function

root.update()
btn.update()
root.protocol('WM_DELETE_WINDOW', close) #assigning close function to the app termination
root.mainloop()




