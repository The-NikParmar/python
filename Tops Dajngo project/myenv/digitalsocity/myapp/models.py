from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique = True,max_length = 30)
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length = 20) # chairman // socity member
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return  self.email + " || " + self.role

class Chairman(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    contect = models.CharField(max_length = 11)
    blockno = models.CharField(max_length = 3)
    houseno = models.CharField(max_length = 4) 
    pic = models.FileField(upload_to="media/upload", default="pic-1.jpg")

    def __str__(self):
        return self.firstname + " || " + self.blockno 
    
<<<<<<< HEAD
class Member(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    contect = models.CharField(max_length = 11)
    blockno = models.CharField(max_length = 3)
    houseno = models.CharField(max_length = 4) 
    occupation = models.CharField(max_length=50)
    job_address = models.TextField()
    bloodgroup = models.CharField(max_length = 3)
    vehical_details = models.CharField(max_length = 20)
    
    pic = models.FileField(upload_to="media/upload", default="pic-1.jpg")
=======
    
  
>>>>>>> f63bfb2bb64648de7493a22aeb84adea06032096
