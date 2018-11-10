import matplotlib.pyplot as plt

 # X  Co-Ordinates  representing courses
left = [20, 30, 40, 50, 60, 70]

 #Y Co=Ordinates representing marks secured
right = [13, 27, 24, 45, 59, 66]
 #Labels  for each bar
tick_label = ['Hisrory','Python','Physics','Eletronics','Math','Proc']

 #Plotting a bar chart 
plt.bar(left, right, tick_label = tick_label,width = 1, color=['blue','pink','yellow','red','green','orange'])

 #Naming the X axis
plt.xlabel('Maximum marks')

 #Naming the Y axis
plt.ylabel('Marks secured')

 #Plot title
plt.title('Graph for representing marks in internals')

 #Function to show the plot
plt.show()




