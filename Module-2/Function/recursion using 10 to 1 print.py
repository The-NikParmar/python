def  num(n):
    print(n)
    if n<=1:
        return 0
    else:
        return num(n-1)
    
num(10)
    
