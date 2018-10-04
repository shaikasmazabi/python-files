#Importing random package
import random
a=['r','p','s']
#Intialising the number of times Computer won
s1=0
#Intialising the number of times You won
s2=0
while(True):
	p=input(" Enter Your Choice r/p/s  :     ")
	#Printing the random choice
	c=random.choice(a)
	
	print("You opt for ",p,"Computer opt for " ,c)
	if(p=='r' or p=='p'or p=="s"):
		if(p==c):
			print("tie")
		elif((p=='r' and c=='p') or(p=='p' and c=='s') or(p=='s' and c=='r')):
			s1=s1+1
			print("Computer won",s1 ,"times")
		else:
			s2=s2+1
			print("U Won",s2 ,"times")
	else:
		print("Improper Input")	
		break
	if(s1==3 or s2==3):
		if(s1==3):
			print("I'M Sorry, Computer Won the game")
		else:
			print("Congratulations!...... You Won against Computer, Have a Wonderful day")
		break	
