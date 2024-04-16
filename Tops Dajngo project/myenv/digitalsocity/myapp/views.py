from django.shortcuts import render,HttpResponsePermanentRedirect
from .models import *
from django.urls import reverse
# Create your views here.

def home(request):
    # Check if the user is logged in by verifying if their email is in the session
    if "email" in request.session:
        # Retrieve the User object based on the email stored in the session
        uid = User.objects.get(email=request.session['email'])
        
        # Retrieve the Chairman object based on the User object
        cid = Chairman.objects.get(userid=uid)

        # Prepare the context to pass to the template
        context = {
            'uid': uid,
            'cid': cid,
        }

        # Render the home page with the retrieved User and Chairman objects
        return render(request, "myapp/index.html", context)
    else:
        # If the user is not logged in, render the login page
        return render(request, "myapp/login.html")

# Login Logic 
def login(request):
    if "email" in request.session:

        # uid = User.objects.get(email=request.session["email"])
        # cid = Chairman.objects.get(userid = uid)
        # context = {
        #     'uid' : uid,
        #     'cid' : cid,
        # }
        # return render(request, "myapp/index.html",context)

        return HttpResponsePermanentRedirect(reverse('home'))
    else:
        if request.POST: 
            try:
                p_email = request.POST["email"]
                p_password = request.POST["password"]
                print(">>>>>>>>>>>>>load page",p_email)
                uid = User.objects.get(email = p_email,password = p_password)
                print("================ Data Get Successful ===============",uid)
                print(f"=============={uid}=================")

                cid = Chairman.objects.get(userid = uid)
                print("==========First Name",cid.firstname)

                request.session['email'] = uid.email

                return render(request,"myapp/index.html")
            
            except Exception as e:
                print("===============>>>>",e)
                msg = "invalid Password or email"
                return render(request,"myapp/login.html",{'e_msg':msg})
        else:
            print("===========page load==========")
            return render(request,"myapp/login.html")  
        
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return HttpResponsePermanentRedirect(reverse("login"))
    else:
        return HttpResponsePermanentRedirect(reverse("login"))
    


def profile(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        context={
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"myapp/profile.html",context)
    else:
        return HttpResponsePermanentRedirect(reverse("login"))


def change_password(request):
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']

        if uid.password == currentpassword:
            uid.password = newpassword
            uid.save()
            context={
                'uid' : uid,
                'cid' : cid,
            }
            s_msg = "successfully password change"
            del request.session['email']
            return render(request,"myapp/login.html",{'s_msg': s_msg})


        else:
            e_msg = "invalid current password"
            del request.session['email']
            return render(request,"myapp/login.html",{'e_msg':e_msg})

def change_profile (request):
     if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)

        if request.POST:
            cid.firstname = request.POST['firstName']
            cid.lastname = request.POST['lastName']
            cid.contect = request.POST['contact']
            cid.blockno = request.POST['block']
            cid.houseno = request.POST['houseno']
            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']
            cid.save()

        context={
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"myapp/profile.html",context)

def add_member(request): 
    if "email" in request.session:
        uid=User.objects.get(email = request.session['email'])
        cid=Chairman.objects.get(userid = uid)
        if request.POST:
            print(">>>>>>>>>>Add Opration")
        context={
                'uid' : uid,
                'cid' : cid,
            }
        return render(request,"myapp/addmember.html",context)
    
     
    


        
