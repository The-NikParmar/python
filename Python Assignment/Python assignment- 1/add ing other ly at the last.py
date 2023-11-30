string=input("enter your string")

if len(string) < 3:
    exit()
elif string[-3:] == 'ing':
  print(string + 'ly')
else:
  print(string + 'ing')
