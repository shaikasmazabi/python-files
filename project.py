import RPi.GPIO as G
import time

trig=17 #GPIO 17
echo=27 
mri8a=12 #GPIO 12
mri8b=16
mlfa=20
mlfb=21
leftir=24 
ri8ir=23

G.setmode(G.BCM)
G.setwarnings(False)
G.setup(trig,G.OUT)
G.setup(echo,G.IN)
G.setup(mri8a,G.OUT)
G.setup(mri8b,G.OUT)
G.setup(mlfa,G.OUT)
G.setup(mlfb,G.OUT)

G.output(trig, True) 
time.sleep(0.001) 
G.output(trig, False) 
time.sleep(2)


# To STOP
def stop():
	G.output(mri8a,False)
	G.output(mri8b,False)
	G.output(mlfa,False)
	G.output(mlfb, False)

# MOVE FORWARD COMMAND
def movefw():
	G.output(mri8a, True)
	G.output(mri8b, False)
	G.output(mlfa, True)
	G.output(mlfb,False)

# Move backwards command
def movebk():
	G.output(mri8a, False)
	G.output(mri8b, True)
	G.output(mlfa, False)
	G.output(mlfb,True)

# Move ri8
def ri8():
	G.output(mri8a,False)
	G.output(mri8b,False)
	G.output(mlfa,True)
	G.output(mlfb,False)

def left():
	G.output(mri8a,True)
	G.output(mri8b,False)
	G.output(mlfa,False)
	G.output(mlfb,False)


while True:

	if(G.input(leftir)==False):
		left()
		time.sleep(0.5)

	if(G.input(ri8ir)==False):
		ri8()
		time.sleep(0.5)

	if(G.input(leftir)==True):
		movefw()

	if(G.input(ri8ir)==True):
		movebk()

	

	







