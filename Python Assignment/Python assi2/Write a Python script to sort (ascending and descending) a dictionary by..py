#  Write a Python script to sort (ascending and descending) a dictionary by value.

dt = {2:'Nik',56:'Smit',23:'Purshottam',1:'Mohit',1:'dax'}

# sorting to asceding order using sorted function 
sorted_dt_value = sorted(dt.items())
print("ascending order dictionary by value:- ",sorted_dt_value)

# sorting to descending orde using sorted function
sorted_dt_value = sorted(dt.items(),reverse=True)
print("descending order dictionary by value:-",sorted_dt_value)

