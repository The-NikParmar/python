#  Write a Python script to sort (ascending and descending) a dictionary by value.

dt = {'Nik':2,'Smit':56,'Purshottam':23,'Mohit':1,'dax':8}

# sorting to asceding order using sorted function 
sorted_dt_value = sorted(dt.values())
print("ascending order dictionary by value:- ",sorted_dt_value)

# sorting to descending orde using sorted function
sorted_dt_value = sorted(dt.values(),reverse=True)
print("descending order dictionary by value:-",sorted_dt_value)

