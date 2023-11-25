class student:
    def name (self,n,a,m):

        self.name=n
        self.age=a
        self.marks=m

class stu:

    def info(self):
        print("Name is :-",self.name)
        print("age is :- ",self.age)
        print("Marks is :- ",self.marks)

class info(stu,student):

    def show(self):

        print("hello")

i=info()

i.name("nik",12,23)
i.info()
i.show()

        
