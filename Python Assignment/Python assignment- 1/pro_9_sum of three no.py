x=int(input("enter your x"))
y=int(input("enter your y"))
z=int(input("enter your z"))

if x == y or y == z or x==z:
    sum = 0
else:
    sum = x + y + z

print("sum of three no ",sum)
