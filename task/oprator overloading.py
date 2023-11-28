# oprator overloading

class score:

    def __init__(self,n):

        self.score=n

    def display(self,y):

        return self.score-y.score

p1=score(30)
p2=score(20)

print(p1.display(p2))

