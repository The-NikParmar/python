''' Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string. '''

a= input("Enter a string:- ")
c=a.find("not")
d=a.find("poor")
if (c>=0 and d>=0):
  a=a.replace(a[c:d+4],"good")
print(a)
