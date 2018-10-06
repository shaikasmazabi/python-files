

a=['1','2','3','4','5','6','7','8','9']

def printB():
	print(a[0], '|' ,a[1], '|' ,a[2])
	print("---------")
	print(a[3], '|' ,a[4], '|' ,a[5])
	print("---------")
	print(a[6], '|' ,a[7], '|' ,a[8])

shaikturn=True
while True:
	print("Your board is ready" )
	printB()

	r=input("Choose an available space  :  ")

	if(r in a):
		if(a[int(r)-1]=='X' or a[int(r)-1]=='O'):
			print("Place is already taken! , Choose another one..........")
			continue
		else:
			if shaikturn:
				print("Shaik's turn >> ")
				a[int(r)-1] = 'X'
				shaikturn = not shaikturn
			else:
				print("Sharon's turn >> ")
				a[int(r)-1] = 'O'
				shaikturn = not shaikturn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("Game Over")
					printB()
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game Over")
					printB()
					exit()
			if(a[0]==a[4] and a[8]==a[4]):
					print("Game Over")
					printB()
					exit()
			elif(a[2]==a[4] and a[2]==a[6]):
					print("Game Over")
					printB()
					exit()



