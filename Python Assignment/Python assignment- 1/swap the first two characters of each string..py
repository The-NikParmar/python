a = input("enter your fist string")
b = input("enter your second string")
print("Before Swap :",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap :",a1," ",b1)
