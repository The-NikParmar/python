import pymysql
mydb = pymysql.connect(host='localhost',user='root',password='',database='topspython')
mycursor = mydb.cursor()


menu = """

    press 1 for add student
    press 2 for update student
    press 3 for delete student
    press 4 for display student
    

"""


def addopration():
    print("======================== ADD STUDENT========================")
    name = input("enter your name : ")
    subject = input("enter subject : ")


    args =(name,subject)
    query = "insert into student (name,subject) values ('%s','%s')"

    mycursor.execute(query%args)
    mydb.commit()
    print("Successfully added !!")
     

def updateopration():
    id = int(input("which student you want to update enter id :"))
    name = input("enter updated name :")
    subject = input("Enter updated subject :")

    query = "update student set name = '%s', subject='%s' where id = %s"
    args = (name,subject,id)

    mycursor.execute(query % args)
    mydb.commit()


def searchstudent():
    name = input("enter your name : ")
    query = "select * from student where name = '%s'"

    args = (name)

    mycursor.execute(query%args)
    res = mycursor.fetchone()
    print(res[0])
    print(res[1])
    print(res[2])

def deletion():
    id = int(input("enter your student id : "))
    query = "delete from student where id = %s"

    args =(id)
    mycursor.execute(query%args)
    mydb.commit()
def display():
    mycursor.execute("select * from student")

    res = mycursor.fetchall()
    for x in res:
        print(x)
    mydb.commit()
status = True

while status:
    print(menu)
    choice = int(input("Enter your choice: "))
    if choice==1:
        addopration()
    elif choice==2:
        updateopration()
    elif choice==3:
        deletion()
    elif choice==4:
        display()
    elif  choice==5:
        searchstudent()



    u_choice = input("do you want perfrom more opration press y for yes and press n for no")

    if u_choice =='y':
        status = True
    else:
        status = False
