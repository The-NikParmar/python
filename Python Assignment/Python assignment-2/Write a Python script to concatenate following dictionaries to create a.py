# Write a Python script to concatenate following dictionaries to create a new one.

di1={"one":1,"Two":2,"Three":3}
di2={"Four":4,"Five":5}

mydi={}

for i in (di1,di2):
    mydi.update(i) # Merage Dictionary 

print("Concating Dictionaries",mydi)
