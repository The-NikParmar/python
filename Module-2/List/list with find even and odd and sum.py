li1=[1,56,34,23,4,34,89,87,56,65,34,31,63,46,87,89,67]

even_sum=0
ecount=0
odd_sum=0
ocount=0


for i in li1:
    if i%2==0:
        even_sum=even_sum+i
        ecount+=1
    else:
        odd_sum=odd_sum+i
        ocount+=1

print(li1)
print("the sum of even No",even_sum)
print("the sum of odd No",odd_sum)
print("the even no of ",ecount)
print("the odd no of ",ocount)
