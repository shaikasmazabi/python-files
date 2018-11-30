import RPi.GPIO as GPIO                    #Import GPIO library
import time

#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

TRIG = 17
ECHO = 27
led = 22

mfr=16#MOTOR FIRST RIGHT
mfl=12#MOTOR FIRST LEFT
msr=21#MOTOR SECOND RIGHT
msl=20#MOTOR SECOND LEFT

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
GPIO.setup(led,GPIO.OUT)                  

GPIO.setup(mfr,GPIO.OUT)
GPIO.setup(mfl,GPIO.OUT)
GPIO.setup(msr,GPIO.OUT)
GPIO.setup(msl,GPIO.OUT)

GPIO.output(led, 1)

time.sleep(5)


#To stop the vehicle all the motors should not work
def stop():
    print "stop"
    GPIO.output(mfr, 0)
    GPIO.output(mfl, 0)
    GPIO.output(msr, 0)
    GPIO.output(msl, 0)

    
#To move forward the first and the seconfd motor's right part should work and left should not work
def forward():
    GPIO.output(mfr, 1)
    GPIO.output(mfl, 0)
    GPIO.output(msr, 1)
    GPIO.output(msl, 0)
    print "Forward"

    
#To move backwards  the first and the seconfd motor's left part should work and right should not work
def back():
    GPIO.output(mfr, 0)
    GPIO.output(mfl, 1)
    GPIO.output(msr, 0)
    GPIO.output(msl, 1)
    print "back"

def left():
    GPIO.output(mfr, 0)
    GPIO.output(mfl, 0)
    GPIO.output(msr, 1)
    GPIO.output(msl, 0)
    print "left"

def right():
    GPIO.output(mfr, 1)
    GPIO.output(mfl, 0)
    GPIO.output(msr, 0)
    GPIO.output(msl, 0)
    print "right"

stop()
count=0
while True:
 i=0
 avgDistance=0
 for i in range(5):
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  time.sleep(0.1)                                   #Delay

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                           #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
       GPIO.output(led, False)             
  pulse_start = time.time()

  while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
       GPIO.output(led, False) 
  pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
  distance = round(distance,2)                 #Round to two decimal points
  avgDistance=avgDistance+distance

 avgDistance=avgDistance/5
 print avgDistance
 flag=0
 if avgDistance < 15:      #Check whether the distance is within 15 cm range
    count=count+1
    stop()
    time.sleep(1)
    back()
    time.sleep(1.5)
    if (count%3 ==1) & (flag==0):
     right()
     flag=1
    else:
     left()
     flag=0
    time.sleep(1.5)
    stop()
    time.sleep(1)
 else:
    forward()
    flag=0
