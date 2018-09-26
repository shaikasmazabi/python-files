#Declaring results of a student

#Submiting the marks secured by the student
m=int(input("Enter the marks secured in Maths : "))
p=int(input("Enter the marks secured in Physics : "))
c=int(input("Enter the marks secured in Chemistry : "))
s=int(input("Enter the marks secured in Computer Science : "))


#Checking whether the student has Failed in any one PCMCs Course
if(m<=34):
	print("Student has failed in Mathematics")
if(p<=34):
	print("Student has failed in Physics")
if(c<=34):
	print("Student has failed in Chemistry")
if(s<=34):
	print("Student has failed in Computer Science")


#Calculating the Total and the Average
Total=m+p+c+s
Avg=Total/4


#Declaring the Results
if(Avg==100):
	print("Student has secured 100% Results")
elif(Avg>=85):
	print("Student has secured Distinction")
elif(Avg>=75):
	print("Student has secured First Class")
elif(Avg>=60):
	print("Student has seccured Second Class")
elif(Avg>=35):
	print("Student has secured Third Class")
else:
	print("Student has Failed")
