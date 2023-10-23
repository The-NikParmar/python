'''

Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.

'''


li=[]
sq=[]
for i in range(1,31):
   li.append(i)
   sq.append(i*i)

print("The lis of  Elements ",li)

print("first five Elements squre",sq[:5])

print("last five Elements squre",sq[-5:])
