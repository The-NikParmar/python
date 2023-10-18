# access dictionary

d1 = {'k1':1,'k2':2,'k3':3,'k1':"hello"}

d2 = {'k2':67,'k5':90}

# return value hold by key
print(d1['k1'])

# value assignment / or can change (dicts are mutable)
d1['k2']=90

# add new element to dicitonary
d1['k4']=78

# update the dictinary

d1.update(d2)

# copy one dict to another

dx={'k1':90,'k2':3}
dx=d2.copy()

print("Copied dictionary : ",dx)

print(d1)
