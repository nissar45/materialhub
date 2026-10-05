from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import *


def login_get(request):
    return render(request,'login.html')
# Code.html (login_post view)

def login_post(request):
    username = request.POST['username']
    password = request.POST['password']

    if not username or not password:
        messages.warning(request, "Username and password is required")
        return redirect('/myapp/login-get')

    check = authenticate(request, username=username, password=password)

    if check is not None:
        login(request, check)

        if check.groups.filter(name='admin').exists():
            return redirect('/myapp/adminhome_get/')
        elif check.groups.filter(name='user').exists():
            return redirect('/myapp/userhome_get/')
        elif check.groups.filter(name='driver').exists():
            return redirect('/myapp/driverhome_get/')

    else:
        messages.warning(request, "User not found")
        return redirect('/myapp/login_get')

    messages.warning(request, "Invalid username or password")
    return redirect('/myapp/login_get')


def adminhome_get(request):
    return render(request,'admin/adminhome.html')

def allocationclient_get(request,id):
    d=Driver.objects.all()
    return render(request,'admin/allocationclient.html',{'data':d,'id':id})

def allocationclient_post(request):
    id = request.POST['id']
    driver = request.POST['driver']


    a=Allocation()
    a.DRIVER_id=driver
    a.REQUEST_id=id
    a.date=datetime.now()
    a.status="pending"
    a.save()


    return redirect('/myapp/view_approve_user_request/#a')


def add_material_get(request):
    return render(request,'admin/add_material.html')

def add_material_post(request):
    name=request.POST['name']
    type=request.POST['type']
    about=request.POST['about']
    amount=request.POST['amount']
    photo=request.FILES['photo']

    fs=FileSystemStorage()
    date=datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
    fs.save(date,photo)
    path=fs.url(date)

    a=Materials()
    a.name=name
    a.type=type
    a.about=about
    a.photo=path
    a.amount=amount
    a.save()
    return redirect('/myapp/view_material_get/#a')


def view_material_get(request):
    a=Materials.objects.all()
    return render(request,'admin/view_material.html',{'data':a})

def edit_material_get(request,id):
    a=Materials.objects.get(id=id)
    return render(request,'admin/edit_material.html',{'data':a})

def edit_material_post(request):
    name = request.POST['name']
    type = request.POST['type']
    about = request.POST['about']
    amount = request.POST['amount']
    id = request.POST['id']

    a = Materials.objects.get(id=id)


    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        fs = FileSystemStorage()
        date = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path
        a.save()

    a.name = name
    a.type = type
    a.about = about
    a.amount = amount
    a.save()
    return redirect('/myapp/view_material_get/#a')



def deletematerial_get(request,id):
    Materials.objects.get(id=id).delete()
    return redirect('/myapp/view_material_get/#a')



def add_stock_get(request):
    a=Materials.objects.all()
    return render(request,'admin/stockadd.html',{'data':a})


def add_stock_post(request):
    name = request.POST['name']
    stock = request.POST['stock']

    a=Stock()
    a.date=datetime.now().date()
    a.stock_no=int(stock)
    a.MATERIAL_id=name
    a.save()
    return redirect('/myapp/view_stock_get/#a')


def edit_stock_get(request,id):
    a=Stock.objects.get(id=id)
    b=Materials.objects.all()
    return render(request,'admin/stockedit.html',{'data':a,'data1':b})


def edit_stock_post(request):
    name = request.POST['name']
    stock = request.POST['stock']
    id = request.POST['id']

    a = Stock.objects.get(id=id)
    a.date = datetime.now().date()
    a.stock_no = int(stock)
    a.MATERIAL_id = name
    a.save()
    return redirect('/myapp/view_stock_get/#a')


def view_stock_get(request):
    a=Stock.objects.all()
    return render(request,'admin/stockview.html',{'data':a})

def deletestock_get(request,id):
    Stock.objects.get(id=id).delete()
    return redirect('/myapp/view_stock_get/#a')


def delete_stock_get(request):
    return redirect('/myapp/view_stock_get/#a')


def edit_driver_get(request,id):
    a=Driver.objects.get(id=id)
    return render(request,'admin/editdriver.html',{'data':a})


def edit_driver_post(request):
    name=request.POST['name']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    number=request.POST['number']
    email=request.POST['email']
    id=request.POST['id']
    a=Driver.objects.get(id=id)


    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        fs = FileSystemStorage()
        date = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path
        a.save()

    if 'proof' in request.FILES:
        proof = request.FILES['proof']

        fs1 = FileSystemStorage()
        date1 = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs1.save(date1, proof)
        path1 = fs1.url(date1)
        a.proof = path1
        a.save()

    a.name=name
    a.place=place
    a.pin=pin
    a.post=post
    a.number=number
    a.email=email
    a.save()
    return redirect('/myapp/view_driver_get/')


def add_driver_get(request):
    return render(request,'admin/driveradd.html')


def add_driver_post(request):
    name=request.POST['name']
    photo=request.FILES['photo']

    fs=FileSystemStorage()
    date = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs.save(date, photo)
    path = fs.url(date)

    proof=request.FILES['proof']

    fs1 = FileSystemStorage()
    date1 = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs1.save(date1, proof)
    path1 = fs1.url(date1)

    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    number=request.POST['number']
    email=request.POST['email']

    user=User.objects.create_user(username=email,password=number)
    user.groups.add(Group.objects.get(name='driver'))

    a=Driver()
    a.name=name
    a.photo=path
    a.proof=path1
    a.place=place
    a.pin=pin
    a.post=post
    a.number=number
    a.email=email
    a.AUTHUSER=user
    a.save()
    return redirect('/myapp/view_driver_get/')


def view_driver_get(request):
    a=Driver.objects.all()
    return render(request,'admin/viewdriver.html',{'data':a})


def delete_driver_get(request,id):
    Driver.objects.get(AUTHUSER=id).delete()
    User.objects.get(id=id).delete()
    return redirect('/myapp/view_driver_get/')

def view_user_request_get(request):
    a=User_request.objects.filter(status="pending")
    return render(request,'admin/userrequest.html',{'data':a})

def approve_user_request(request,id):
    User_request.objects.filter(id=id).update(status='approved')
    return redirect('/myapp/view_approve_user_request/')


def reject_user_request(request,id):
    User_request.objects.filter(id=id).update(status="rejected")
    return redirect('/myapp/view_rejected_user_request/')

def view_approve_user_request(request):
    a = User_request.objects.filter(status="approved")
    return render(request,'admin/view_approve_request.html',{'data':a})

def view_rejected_user_request(request):
    a = User_request.objects.filter(status="rejected")
    return render(request,'admin/view_rejected_request.html',{'data':a})

def view_complaint_get(request):
    a=Complaint.objects.all()
    return render(request,'admin/view_Complaint.html',{'data':a})

def sentreply_get(request,id):
    a=Complaint.objects.get(id=id)
    return render(request,'admin/sentreply.html',{'data':a})

def sentreply_post(request):
    reply=request.POST['reply']
    id=request.POST['id']
    a=Complaint.objects.get(id=id)
    a.reply=reply
    a.status="replied"
    a.save()
    return redirect('/myapp/view_complaint_get/')

def changepassword_get(request):
    return render(request,'admin/changepassword.html')

def changepassword_post(request):
    current=request.POST['current']
    new=request.POST['new']
    confirm=request.POST['confirm']


    user=request.user
    if user.check_password(current):
        if new==confirm:
            user.set_password(new)
            user.save()
            logout(request)
            return redirect('/myapp/login_get/')
        else:
            return redirect('/myapp/changepassword_get/')
    else:
        return redirect('/myapp/changepassword_get/')

# driver.............................

def d_changepassword_get(request):
    return render(request,'driver/changepassword.html')

def d_changepassword_post(request):
    return redirect('/myapp//')

def viewallocation_get(request):
    data=Allocation.objects.filter(DRIVER__AUTHUSER=request.user)
    print(data)
    print(request.user)
    return render(request,'Driver/viewallocation.html',{'data':data})

def viewprofile_get(request):
    a=Driver.objects.get(AUTHUSER=request.user)
    return render(request,'driver/viewprofile.html',{'data':a})

def updatestatus(request,id):
    Allocation.objects.filter(id=id).update(status='completed')
    return redirect('/myapp/viewallocation_get/')

#user......................................

def editprofile_get(request,id):
    b=Users.objects.get(id=id)
    return render(request,'user/editprofile.html',{'data':b})

def editprofile_post(request):
    name = request.POST["name"]
    number = request.POST["number"]
    email = request.POST["email"]
    place = request.POST["place"]
    pin = request.POST["pin"]
    id = request.POST["id"]
    a = Users.objects.get(id=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        fs = FileSystemStorage()
        date = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(date, photo)
        path1 = fs.url(date)
        a.photo = path1
        a.save()

    a.name = name
    a.number = number
    a.email = email
    a.place = place
    a.pin = pin
    a.save()
    return redirect('/myapp/userviewprofile_get/')

def materialclient_get(request):
    a=Materials.objects.all()
    return render(request,'user/materialclient.html',{'data':a})\

def viewrequeststatus(request):
    a=User_request.objects.filter(USERS__AUTHUSER=request.user)
    return render(request,'user/viewrequeststatus.html',{'data':a})

def mmaterialclientquntyy_get(request,id):
    a=Materials.objects.get(id=id)
    return render(request,'user/mmaterialclientquntyy.html',{'data':a})

def mmaterialclientquntyy_post(request):
    id=request.POST['id']
    quantity=request.POST['quantity']
    a=User_request()
    a.quantity=quantity
    a.date=datetime.now().today()
    a.status='pending'
    a.MATERIAL=Materials.objects.get(id=id)
    a.USERS=Users.objects.get(AUTHUSER=request.user)
    a.save()
    return redirect('/myapp/viewrequeststatus/')

def paymenthistoryclient_get(request):
    a=Payment.objects.filter(USERS__AUTHUSER=request.user)
    return render(request,'user/paymenthistoryclient.html',{'data':a})

def sendcomplaint_get(request):
    return render(request,'user/sendcomplaint.html')

def sendcomplaint_post(request):
    complaint=request.POST['complaint']

    a=Complaint()
    a.complaint=complaint
    a.date=datetime.now().today()
    a.status='pending'
    a.reply='pending'
    a.USERS=Users.objects.get(AUTHUSER=request.user)
    a.save()
    return redirect('/myapp/view_reply_get/')

def signupclient_get(request):
    return render(request,'user/signupclient.html')

def signupclient_post(request):
    name= request.POST["name"]
    number= request.POST["number"]
    email= request.POST["email"]
    place= request.POST["place"]
    pin= request.POST["pin"]
    password= request.POST["password"]
    photo= request.FILES["photo"]

    fs1 = FileSystemStorage()
    date1 = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs1.save(date1, photo)
    path1 = fs1.url(date1)

    user = User.objects.create_user(username=email, password=password)
    user.groups.add(Group.objects.get(name='user'))

    a=Users()
    a.name=name
    a.number=number
    a.email=email
    a.place=place
    a.pin=pin
    a.photo=path1
    a.AUTHUSER=user
    a.save()
    return redirect('/myapp/login_get/')

def userhome_get(request):
    return render(request,'user/UserHome.html')

def userchangepassword_get(request):
    return render(request,'user/userchangepassword.html')

def userchangepassword_post(request):
    return redirect('/myapp//')

def view_reply_get(request):
    a=Complaint.objects.filter(USERS__AUTHUSER=request.user)
    return render(request,'user/view_reply.html',{'data':a})

def userviewprofile_get(request):
    a=Users.objects.get(AUTHUSER=request.user)
    return render(request,'user/viewprofile.html',{'data':a})


def user_changepassword_get(request):
    return render(request,'user/userchangepassword.html')

def user_changepassword_post(request):
    current=request.POST['current']
    new=request.POST['new']
    confirm=request.POST['confirm']


    user=request.user
    if user.check_password(current):
        if new==confirm:
            user.set_password(new)
            user.save()
            logout(request)
            return redirect('/myapp/login_get/')
        else:
            return redirect('/myapp/userchangepassword_get/')
    else:
        return redirect('/myapp/userchangepassword_get/')


def driverhome_get(request):
    return render(request,'Driver/DriverHome.html')
