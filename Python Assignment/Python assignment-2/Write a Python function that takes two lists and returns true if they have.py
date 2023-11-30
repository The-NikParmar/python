#Write a Python function that takes two lists and returns true if they have at least one common member.

def common(list1, list2):
    # Using set  to find common elements
    same_member = set(list1) & set(list2)
    
    # If there are common elements, return True otherwise, return False
    return bool(same_member)

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

result = common(list_a, list_b)
print(result)

                 
