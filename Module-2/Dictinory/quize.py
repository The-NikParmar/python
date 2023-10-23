Quize={}
q=1
a=1
for i in range(3):
    Que=input(f"Enter your Question: {q}:")
    ans=input(f"Enter your ans: {a}:")
    q+=1
    a+=1
    
    Quize.update({Que:ans})
print(Quize)

print("=============Start Game=============")

Score=0
q=1
for i,a in Quize.items():
    print(f"Your Question {q}:- {i}")
    ans=input("Enter Your Answer")
    q+=1
    if ans==a:
        Score+=5
    else:
        Score-=10

print("your score is",Score)
    
