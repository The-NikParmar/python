#Write a Python script to merge two Python dictionaries.

dic1={'one':1,'two':2,'three':3}
dic2={'four':4,'five':5,'six':6} # two Diffrent Dictionary 

dic={}

#convert Dictionary to list 
res=list(dic1.items())
res1=list(dic2.items())

for i in res1:
    res.append(i) # Two list merge
    
dic=dict(res) # Converrt list to Dictionary 
print("Merge Two Dictionary ",dic)# print two Merge Dictionary 

# Second method 

'''
for i in dic2:
     dic1.update(i)
print(dic1)
'''
