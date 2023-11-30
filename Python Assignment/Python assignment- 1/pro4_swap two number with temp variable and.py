print("Using with temp variable") 
no1=int(input("enter your no1"))
no2=int(input("enter your no2"))

temp=no1
no1=no2
no2=temp

print("Swap value")
print("no1 is: ",no1)
print("no2 is: ",no2)

print("without third variable swaping")

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
print("A = {} and B = {}".format(a, b))
a = a + b
b = a - b
a = a - b
print("Now, A = {} and B = {}".format(a, b))
