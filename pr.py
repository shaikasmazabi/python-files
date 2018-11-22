import RPi.GPIO as R
import time


R.setmode(R.BCM)
R.setup(4,R.IN)
R.setup(14,R.IN)
R.setup(17,R.OUT)#trigger
R.setup(27,R.IN)#echo

while True:
    if avgD
    if(R.input(4)==True and R.input(14)==True):
        print("Moving Forward.........")
        time.sleep(2)
    elif(R.input(4)==True and R.input(14)==False):
        print("Moving RIGHT TURN.........")
        time.sleep(2)
    elif(R.input(4)==False and R.input(14)==True):
        print("Moving LEFT TURN.........")
        time.sleep(2)
    else:
        print("STOP")
    
