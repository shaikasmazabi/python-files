#Playing the game Snake and Ladder with only rolling the dice and getting the random numbers with Shaik, Sarah , Sandeep

import random
if(k)
while True:
	i=input("Enter 'q' to quit : ")
	if(i=='q'):
		print("Thank You for being with us, Have a nice day")
		print("Good Bye")
		exit()
	elif(i=='s'):
		print("Congratulations Shaik , U have got the number",random.randint(1,6))

	elif(i=='t'):
		print("Congratulations Sarah, U have got the number",random.randint(1,6))
	elif(i=='d'):
		print("Congratulations Sandeep, U have got the number",random.randint(1,6))

	else:
		print("Please press 'r' to roll , 'q' to quit")