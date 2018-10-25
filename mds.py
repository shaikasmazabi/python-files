import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin,GPIO.IN)
count=1
time.sleep(3)
a=56
while count<=4:
    
    if GPIO.input(pirPin):
        print("Motion detected")
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/saraht/"+str(a)+".jpg")
        print("Pic taken")
        time.sleep(1)
        count = count + 1
        a=a+1
print("Testing")
exit()

        
        
