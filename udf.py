#Performing Functions

#Asking user to input values of a and b to perform some basic operations using functions
a=int(input("Enter a number : "))
b=int(input("Enter another number : "))

#Defining add function
def add():
  return a+b

#Defining sub function
def sub():
     return a-b

#Defining mul function
def mul():
	return a*b

#Defining sqa function
def sqa():
	return a*a

#Defining sqb function
def sqb():
	return b*b


#Defining cua function
def cua():
	return a*a*a

#We are calling the already defined functions

#Calling add function and printing the result
print("Addition of ",a , "and" ,b,"is")
d=add()#Calling the add function
print(d)#Printing the result

#Calling sub function and printing the result
print("Subtraction of ",a, "from" ,b, "is",sub())

#Calling mul function and printing the result
print("Multiplication of" ,a, "and" ,b, "is",mul())

#Calling sqa function and printing the result
print("Square of ",a, "is",sqa())

#Calling sqb function and printing the result
print("Square of ",b, "is",sqb())

#Calling cua function and printing the result
print("Cube of",a,"is",cua())






