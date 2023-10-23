 #  Write a Python program to count the occurrences of each word in agiven sentence

st=("python is easy to learn ")
count = dict()

count =st.split()
print(count)

for i in st:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print("the number of characters",count)
    

