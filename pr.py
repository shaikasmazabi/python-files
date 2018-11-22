import RPi.GPIO as R
import time


R.setmode(R.BCM)
R.setup(4,R.IN)
R.setup(14,R.IN)
R.setup(17,R.OUT)#trigger
R.setup(27,R.IN)#echo



 
while True:
    #Set Trigger to 
    def distance():
         HIGH
         R.output(17,True)

    #Set trigger after 0.01ms to LOW time.sleep(0.00001)
    R.output(17,False)

    StartTime=time.time()
    StopTime=time.time()

    #Save Start Time
    while R.input(27)==0:
            StartTime=time.time()
        
      #Save time for arrival
    while R.input(27)==1:
            StopTime=time.time()
        
    
    pulse_start = time.time()
    while R.input(27)==1:
        #Check whether the ECHO is HIGH
        R.output(led, False) 
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)

    if(distance<8):
        print("Turn RI8")
        time.sleep(2)

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
    
