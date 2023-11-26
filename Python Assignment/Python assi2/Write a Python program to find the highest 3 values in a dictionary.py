dt = {'Nik': 1, 'smit': 34, 'Purshottam': 98, 'Apple': 78, 'Oppo': 60, 'vivo': 93}

# Sorting the dictionary  values in descending order
sorted_items = sorted(dt.items(), key=lambda x: x[1], reverse=True)

# Selecting the top 3 items from the sorted list and converting it back to a dictionary
result = dict(sorted_items[:3])

print(result)
