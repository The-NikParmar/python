count = 0

f = open("myfile.txt","r")


d = f.read()

data = d.split()

for w in data:

    if not w.isnumeric():
        count +1
        print(w)

print(count)