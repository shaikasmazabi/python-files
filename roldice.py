import random


while True:
	i=input("Enter q to quit : ")
	if(i=='q'):
		print("Bye!")
		print("Have nice day")
		exit()
	elif(i=='r'):
		print("You rolled the number" ,random.randint(1,6))
	else:
		print("Press 'r' to roll the dice ,'q' to quit ")