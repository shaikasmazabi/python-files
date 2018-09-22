#Implementing conditions like IF , ELSE IF , ELSEIF-LADDER
x=int(input("Enter a number : "))
#Checking whether the number is even or odd using if condition
if(x%2==0):
     print(x,"is an even number")
if(x%2!=0):
     print(x, "is an odd number")
#Checking whether the number is a positive,zero or a negative number using elif - ladder condition
if(x>0):
	print(x, "is a positive number")
elif(x==0):
	print(x, "is zero")
else:
	print(x, "is a negative number")
#Finding the greatest number using if else condition
y=int(input("Enter another number : "))
if(x>y):
	print(x, "is greater than " ,y)
else:
	print(y, "is greater than " ,x)
	


