#Playing Snake and Ladder game 


#The initial position of the player is being assigned to the variable 'n'
n=0

#we are importing random package to get random numbers when we roll the dice
import random
while(n<100):
	a=input("Enter 'r' to the roll the dice and 'q' to quit : ")
	if(a=='r'):
		#Rolling the dice and getting random numbers between 1 to 6
		r=random.randint(1,6)

		#We are updating the new position
		n=n+r

		#We are printing the number we rolled on the dice
		print("You have rolled the number",r)

		#We are printing the new updated position of the player
		print("Your new position is ",n)


		#Checking for some Snakes and Ladders in your position 'n'

		#Checking for the Ladder
		if(n==8):
			n=37
			print("Congratulations, You have got a ladder")
		#Checking for a Snake
		elif(n==11):
			n=2
			print("Sorry, You have been bit by a snake")
		#Checking for a Ladder
		elif(n==13):
			n=34
			print("Congratulations, You have got a ladder")
		#Checking for a Snake
		elif(n==25):
			n=4
			print("Sorry, You have been bit by a snake")
		#Checking for a Snake
		elif(n==38):
			n=9
			print("Sorry, You have been bit by a snake")
		#Checking for a Ladder
		elif(n==40):
			n=68
			print("Congratulations, You have got a ladder")
		#Checking for a Ladder
		elif(n==52):
			n=81
			print("Congratulations, You have got a ladder")
		#Checking for a Snake
		elif(n==65):
			n=46
			print("Sorry, You have been bit by a snake")
		#Checking for a Ladder
		elif(n==76):
			n=97
			print("Congratulations, You have got a ladder")
		#Checking for a Snake
		elif(n==89):
			n=70
			print("Sorry, You have been bit by a snake")
		#Checking for a Snake
		elif(n==93):
			n=64
			print("Sorry, You have been bit by a snake")
		#Checking whether if you have got the number 100
		elif(n==100):
			#Printing that you are the winner
			print("Eurekha!... You are the Winner")
			exit()
		#Checking whether you got the number more than 100
		elif(n>100):
			#Printing that you have to stay at the same place
			print("Unfortunately U have crossed the number 100 , So You stay at the same place")
			n=n-r









