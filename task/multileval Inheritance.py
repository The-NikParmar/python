class Player:

    def name (self):
        print("virat")

class Player2(Player):

    def run(self):
        print("virat total run is 322")

class Player3(Player2):

    def age (self):
        print("virat  age is 34")

p1=Player3()

p1.name()
p1.run()
p1.age()
        
