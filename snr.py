import random



while True:
	i=input("Enter 'q' to quit : ")
	if(i=='q'):
		print("Thank You for being with us, Have a nice day")
		print("Good Bye")
		exit()
	else:
		print("You have rolled the number",random.randint(1,6))