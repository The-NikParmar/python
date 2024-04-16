'''
there are 2 type of exception


1) bulit - in  exceptio
2) user define or custom exception:


which is create by user and we can call as per requrment

'''


class Myexception(Exception):
    pass

try:
    num = int(input("Enter a number"))
    if num<0:
        raise Myexception
    
except Myexception:
    print("no must be positive")