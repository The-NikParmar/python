import sys

try:
    print(a)

except:
    print("something went wrong")
    print(sys.exc_info())
    print(sys.exc_info[0])
    print(sys.exc_info[1])


'''
try: which is contain code
except: which is similar like catch and handle exception
finally: which always invoke exception occur or not
else: it will run without exception code

'''


try:
    num = int(input("enter a number"))
except:
    print("invalid input")
finally:
    print("Thank you for using this application")