import random
print("Welcome to the game of Rock , Paper , Scissor")
while True:
	i=input("Enter 'r' for Rock , 'p' for Paper , 's' for Scissor  and 'q' to quit the Game :      ")
	a={1:"Rock" , 2:"Paper", 3:"Scissor"}
	o=a[random.randint(1,3)]
	print("Computer has put",o)


	if(i=='q'):
		print("Your choice is to quit the game ")
		print("Hope u had nice time with us ")
		print("Great meeting u")
		print("Good Bye!")
		exit()

	elif(i=='r' and o=='Rock'):
		print("Oh! It's Rock on both sides ")
		print("It's a Tie!..........")
	elif(i=='p' and o=='Paper'):
		print("Oh! It's Paper on both sides ")
		print("It's a Tie!..........")
	elif(i=='s' and o=='Scissor'):
		print("Oh! It's Scissor on both sides ")
		print("It's a Tie!..........")
	elif(i=='p' and o=='Rock'):
	   print("Congratulations!, Paper covers the Rock" , "You Win")
	elif(i=='p' and o=='Scissor'):
	   print("Oops! Scissor cuts the  Paper " , "You Loose")
	elif(i=='r' and o=='Paper'):
	    print("Oops! Paper covers the Rock" , "You Loose")
	elif(i=='r' and o=='Scissor'):
	    print("Congratulations!, Rock hits the Scissor" , "You Win")
	elif(i=='s' and o=='Paper'):
		print("Congratulations! Scissor cuts the  Paper " , "You Win")

	elif(i=='s' and o=='Rock'):
		print("Oops!, Rock hits the Scissor" , "You Loose")
	else:
		exit()
	






