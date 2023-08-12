from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import mysql.connector as sql
from django.db.models import Q
from .models import SignUpData,packages,custom


def sample1(request):
    return render(request,"index.html")

def sample2(request):
    return render(request,"destination.html")

def sample3(request):
    return render(request,"travel.html")

def sample4(request):
    return render(request,"login.html")
# Login database

# def signin(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         if request.method=="POST":
#             username=request.POST['username']
#             password=request.POST["password"]
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 return redirect('/signin')
#         else:
#             return render(request,"login.html")
#
# fn=''
# un=''
# em=''
# ph=''
# pwd=''
# cp=''
# gen=''

def sample5(request):
    return render(request, 'regester.html')
# global fn,un,em,ph,pwd,cp,gen
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="vivek",database='register')
#         cursor = m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="first_name":
#                 fn=value
#             if key=="user_name":
#                 un=value
#             if key=="email":
#                 em=value
#             if key=="number":
#                 ph=value
#             if key=="password":
#                 pwd=value
#             if key=="confirm_password":
#                 cp=value
#             if key=="gender":
#                 gen=value
#         c="insert into register Values('{}','{}','{}','{}','{}','{}','{}')".format(fn,un,em,ph,pwd,cp,gen)
#         cursor.execute(c)
#         m.commit()

def sample6(request):
    return render(request,"user.html")
def sample7(request):
    return render(request,"contact.html")

def sample8(request):
    return render(request,"about.html")


def SignUpDatafunction(request):
    fullname = request.POST['fullname']
    username = request.POST['username']
    email = request.POST['email']
    phonenum = request.POST['phonenum']
    password = request.POST['password']
    signobj = SignUpData(sign_FullName=fullname,sign_Username=username,sign_Email=email,sign_PhoneNumber=phonenum,sign_password=password)
    SignUpData.save(signobj)
    return render(request,"login.html")

def checkuserlogin(request):
    username=request.POST["username"]
    pwd=request.POST["password"]
    flag=SignUpData.objects.filter(Q(sign_Username=username) & Q(sign_password=pwd))
    if flag:
        user = SignUpData.objects.get(sign_Username=username)
        request.session["uname"] = user.sign_Username
        return render(request, "user.html", {"uname": user.sign_Username})
    else:
        return render(request, "logfail.html")


def travel(request):
    r=packages.objects.all()
    return render(request, "travel.html",{"data":r})

def payment(request,id):
    r=packages.objects.filter(pid=id)
    return render(request, "payment.html", {"d": r[0]})

def custom(request):
    country = request.POST['country']
    State = request.POST['State']
    city = request.POST['city']
    Hotels = request.POST['Hotels']
    UserRating = request.POST['UserRating']
    PropertyType = request.POST['PropertyType']
    Chains = request.POST['Chains']
    Amenities = request.POST['Amenities']
    obj=custom(country=country,State=State,city=city,Hotels=Hotels,UserRating=UserRating,PropertyType=PropertyType,Chains=Chains,Amenities=Amenities)
    custom.save(obj)
    r=custom.objects.all()
    return render(request, "customhtm.html",{"data":r})


def addcustom(request):
    return render(request, "custom.html")

def sucpayment(request):
    return render(request, "paymsuc.html")


def searchcity(request,city,days,type,n):
    r=packages.objects.filter(name=city)

    p=r[0]

    return render(request, "te.html",{"name":p.name,"imgurl":p.imgurl,"price":p.price*days,"des":p.des,"pid":p.pid})


def sear(request):
    return render(request, "search.html")

def destination(request):
    r=destination.objects.all()
    return render(request, "destination.html",{"data":r})