from django.shortcuts import render
from.models import State,Login,User,Addresorts,Managerregister,Feedback,Image,Booking
# Create your views here.
from django.http import HttpResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt
import time



def homee(request):

    data = Addresorts.objects.filter(cost=4500)
    data2 = Addresorts.objects.filter(cost=25090)

    return render(request, 'homee.html', {'data': data,'data2':data2})
def logins(request):
    try:
        m=Login.objects.get(username=request.POST['username'],password=request.POST['password'])
        if m.status==1:
           request.session['user']=m.username
           return render(request,'userhome.html')
        elif m.status==2:
             request.session['user']=m.username
             return render(request,'adminhome.html')
        elif m.status==3:
             request.session['user']=m.username
             return render(request,'managerhome.html')
        else:
             return render(request,'login.html',{'error':" your username and password didn't match."})
    except:
          return render(request, 'login.html',{'error': "your username/password didnt match."})

def login(request):
    return render(request,'login.html')
def out(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request, 'login.html')
def register(request):
    s = State.objects.all()
    return render(request,'register.html',{'data':s})
def reg(request):
    name = request.POST['name']
    address = request.POST['address']
    s = request.POST['State']
    insta = State.objects.get(id=s)
    city = request.POST['city']
    pincode = request.POST['pincode']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    photo = request.FILES['file']
    data = User(name=name, address=address,city=city, pincode=pincode, email=email,
                photo=photo, username=username, password=password, state=insta)
    data.save()
    data1 = Login(username=username, password=password, status=1)
    data1.save()
    return render(request,'login.html')
def userprofile(request):
    user = request.session['user']
    data = User.objects.filter(username=user)
    return render(request,'userprofile.html',{'data':data})

def adminhome(request):

    return render(request, 'adminhome.html')
def adminprofile(request):
    user = request.session['user']
    data = Login.objects.filter(username=user)
    return render(request, 'adminprofile.html',{'data':data})
def addresort(request):
    s = State.objects.all()
    return render(request,'addresort.html',{'data':s})
def addre(request):
    resortname = request.POST['resortname']
    place = request.POST['place']
    s = request.POST['State']
    insta = State.objects.get(id=s)
    noofrooms = request.POST['noofrooms']
    cost = request.POST['cost']
    availability = request.POST['availability']
    safty = request.POST['safty']
    activities = request.POST['activities']
    des = request.POST['des']
    facilities = request.POST['facilities']
    photo = request.FILES['file']
    map = request.POST['map']
    user = request.session['user']
    data = Addresorts(resortname=resortname, place=place, noofrooms=noofrooms, cost=cost,
                      availability=availability, safty=safty, activities=activities, des=des, facilities=facilities,
                      photo=photo, map=map,username=user, state=insta)
    data.save()
    return render(request, 'managerhome.html')
def adminaddresort(request):
    s = State.objects.all()
    return render(request,'adminaddresort.html',{'data':s})
def adminaddre(request):
    resortname = request.POST['resortname']
    place = request.POST['place']
    s = request.POST['State']
    insta = State.objects.get(id=s)
    noofrooms = request.POST['noofrooms']
    cost = request.POST['cost']
    availability = request.POST['availability']
    safty = request.POST['safty']
    activities = request.POST['activities']
    des = request.POST['des']
    facilities = request.POST['facilities']
    photo = request.FILES['file']
    map = request.POST['map']
    data = Addresorts(resortname=resortname, place=place, noofrooms=noofrooms, cost=cost,
                      availability=availability, safty=safty, activities=activities, des=des, facilities=facilities,
                      photo=photo, map=map, state=insta)
    data.save()
    return render(request, 'adminhome.html')
def profile(request):
    user = request.session['user']
    data = Addresorts.objects.filter(username=user)
    return render(request,'profile.html',{'data':data})

def userview(request):
    data = User.objects.all()
    return render(request,'userview.html',{'data':data})
def userhome(request):
    user = request.session['user']
    data1 = User.objects.filter(username=user)
    data = Addresorts.objects.all()
    return render(request, 'userhome.html', {'data': data,'data1': data1})
def managerregister(request):
    s = State.objects.all()
    return render(request,'managerregister.html',{'data':s})
def managerreg(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    phone = request.POST['phone']
    address = request.POST['address']
    s = request.POST['State']
    insta = State.objects.get(id=s)
    city = request.POST['city']
    pincode = request.POST['pincode']
    resortname = request.POST['resortname']
    place = request.POST['place']

    designation = request.POST['designation']
    username = request.POST['username']
    password = request.POST['password']
    photo = request.FILES['file']
    data = Managerregister(name=name, dob=dob, gender=gender, phone=phone, address=address, state=insta,
                           city=city, pincode=pincode, resortname=resortname, place=place,
                           designation=designation, photo=photo, username=username, password=password)
    data.save()
    data1 = Login(username=username, password=password, status=3)
    data1.save()
    return render(request,'login.html')
def managerhome(request):
    user = request.session['user']
    data = Managerregister.objects.filter(username=user)
    return render(request,'managerhome.html',{'data':data})
def managerprofile(request):
    user = request.session['user']
    data = Managerregister.objects.filter(username=user)
    return render(request,'managerprofile.html',{'data':data})
def managerprofileupdate(request):
    id = request.POST['id']
    data = Managerregister.objects.filter(id=id)
    return render(request, 'managerprofileupdate.html',{'data':data})
def managerupdateprofile(request):
    id = request.POST['id']
    data = Managerregister.objects.get(id=id)
    data.name = request.POST['name']
    data.gender = request.POST['gender']
    data.phone = request.POST['phone']
    data.address = request.POST['address']
    data.city = request.POST['city']
    data.pincode = request.POST['pincode']

    data.save()
    id = request.POST['id']
    data = Managerregister.objects.filter(id=id)
    return render(request, 'managerprofile.html',{'data':data})

def about(request):
    return render(request, 'about.html')
def det(request):
    id = request.POST['id']
    data = Addresort.objects.filter(id=id)
    return render(request, 'det.html',{'data':data})
def ser(request):
    if request.GET:
       n=request.GET['resortname']
       data=Addresorts.objects.filter(resortname=n)
       return render(request, 'about.html', {'data': data})
    return render(request,'about.html')
def aser(request):
    data = Addresorts.objects.all()
    return render(request, 'userhome.html', {'data': data})
def editfile(request):
    id = request.POST['id']
    data = Addresorts.objects.filter(id=id)
    return render(request, 'editfile.html',{'data':data})
def editresort(request):
    data = Addresorts.objects.all()
    return render(request, 'editresort.html',{'data':data})
def update(request):
    id = request.POST['id']
    data = Addresorts.objects.get(id=id)
    data.resortname = request.POST['resortname']
    data.place = request.POST['place']
    data.noofrooms = request.POST['noofrooms']
    data.cost = request.POST['cost']
    data.availability = request.POST['availability']
    data.safty = request.POST['safty']
    data.activities = request.POST['activities']
    data.des = request.POST['des']
    data.facilities = request.POST['facilities']
    data.photo = request.FILES['img']
    data.save()
    data = Addresorts.objects.all()
    return render(request, 'editresort.html', {'data': data})
def editmanagerresort(request):
       user = request.session['user']
       data = Addresorts.objects.filter(username=user)
       return render(request,'editmanagerresort.html',{'data':data})

def editmanagerfile(request):
    id = request.POST['id']
    data = Addresorts.objects.filter(id=id)
    return render(request, 'editmanagerfile.html',{'data':data})
def managerupdate(request):
    id = request.POST['id']
    data = Addresorts.objects.get(id=id)
    data.resortname = request.POST['resortname']
    data.place = request.POST['place']
    data.noofrooms = request.POST['noofrooms']
    data.cost = request.POST['cost']
    data.availability = request.POST['availability']
    data.safty = request.POST['safty']
    data.activities = request.POST['activities']
    data.des = request.POST['des']
    data.facilities = request.POST['facilities']
    data.photo = request.FILES['img']

    data.save()
    id = request.POST['id']
    data = Addresorts.objects.filter(id=id)
    return render(request, 'editmanagerresort.html', {'data': data})

def resortabout(request):
    return render(request,'resortabout.html')
def contact(request):
    data = Addresorts.objects.all()
    return render(request,'contact.html', {'data': data})
def viewresort(request):
    data = Addresorts.objects.all()
    return render(request, 'viewresort.html', {'data': data})
def viewresorts(request):
    if request.method == 'POST':
        id = request.POST['id']
        data = Addresorts.objects.get(id=id)
        data1 = Feedback.objects.filter(resortname=data)
        data2 = Managerregister.objects.filter(username=data.username)
        return render(request, 'resortmanagerview.html', {'data': data,'data1':data1,'data2':data2})
    return render(request, 'resortmanagerview.html')
def viewbookings(request):
    if request.method == 'POST':
        id = request.POST['id']
        data2 = Booking.objects.get(id=id)
        data = User.objects.filter(username=data2.username)
        return render(request, 'profile.html', {'data': data,'data2':data2})
    return render(request, 'resortmanagerview.html')
def resortmanagerview(request):

    return render(request, 'resortmanagerview.html')

def viewmanager(request):
    data = Managerregister.objects.all()
    return render(request, 'viewmanager.html', {'data': data})


def readmore(request):
     if request.method == 'POST':
        id = request.POST['id']
        data = Addresorts.objects.get(id=id)
        data1 = Feedback.objects.filter(resortname=data)

        data2 = Image.objects.filter(username=data.username)
        return render(request, 'readmore.html', {'data': data, 'data1': data1,'data2':data2})
     return render(request, 'readmore.html')




# Feedbacks

def feedback(request):
    s = Addresorts.objects.all()
    return render(request,'feedback.html',{'data':s})
def adminfeedback(request):
    s = Addresorts.objects.all()
    return render(request,'adminfeedback.html',{'data':s})
def managerfeedback(request):
    s = Addresorts.objects.all()
    return render(request,'managerfeedback.html',{'data':s})
def feedbacks(request):
    resortdetails = request.POST['resortdetails']
    s = request.POST['Resort']
    insta = Addresorts.objects.get(id=s)
    comment = request.POST['comment']
    rating = request.POST['rating']
    user = request.session['user']
    data = Feedback(username=user, resortdetails=resortdetails, comment=comment, rating=rating, resortname=insta)
    data.save()
    return render(request, 'userhome.html')
def managerfeedbacks(request):
    resortdetails = request.POST['resortdetails']
    s = request.POST['Resort']
    insta = Addresorts.objects.get(id=s)
    comment = request.POST['comment']
    rating = request.POST['rating']
    user = request.session['user']
    data = Feedback(username=user, resortdetails=resortdetails, comment=comment, rating=rating, resortname=insta)
    data.save()
    return render(request, 'managerhome.html')
def adminfeedbacks(request):
    resortdetails = request.POST['resortdetails']
    s = request.POST['Resort']
    insta = Addresorts.objects.get(id=s)
    comment = request.POST['comment']
    rating = request.POST['rating']
    user = request.session['user']
    data = Feedback(username=user, resortdetails=resortdetails, comment=comment, rating=rating, resortname=insta)
    data.save()
    return render(request, 'adminhome.html')
def feedbackview(request):
    data =Feedback.objects.all()
    return render(request, 'feedbackview.html', {'data': data})
def userfeedbackview(request):
    user = request.session['user']
    data = Feedback.objects.filter(username=user)
    return render(request, 'userfeedbackview.html',{'data': data})
def resortfeedback(request):
    user = request.session['user']

    data2 = Addresorts.objects.get(username=user)
    data = Feedback.objects.filter(resortname=data2)
    return render(request, 'resortfeedback.html', {'data': data})



def demo(request):
    return render(request, 'demo.html')
def delete(request,id):
    return render(request, 'userview.html')

# Booking

def booknow(request):
    s = Addresorts.objects.all()
    return render(request, 'booknow.html',{'data':s})
def book(request):
    s = request.POST['Resort']
    insta = Addresorts.objects.get(id=s)
    type = request.POST['type']
    acnonac = request.POST['acnonac']
    adult = request.POST['adult']
    child = request.POST['child']
    checkin = request.POST['checkin']
    checkout = request.POST['checkout']
    user = request.session['user']
    data1 = Booking(resortname=insta,type=type, acnonac=acnonac, adult=adult, child=child, checkin=checkin, checkout=checkout,
                   username=user,status=0,valid=0)

    myDate = (time.strftime("%m/%d/%Y"))

    if checkout >= myDate:
        data1.valid = 'Active'

        data1.save()
    else:
        data1.valid = 'Expir'
        data1.save()

    data = Booking.objects.all().last()
    return render(request, 'payments.html',{'data':data})
def mybooking(request):
    user = request.session['user']
    data = Booking.objects.filter(username=user)

    return render(request, 'mybooking.html', {'data': data})
def managerbookview(request):
    user = request.session['user']
    data = Addresorts.objects.get(username=user)
    data2 = Booking.objects.filter(resortname=data)
    return render(request, 'managerbookview.html', {'data2': data2})

def adminbookview(request):

    data = Booking.objects.all()

    return render(request, 'adminbookview.html',{'data': data})

#State

def state(request):
    return render(request, 'state.html')
def states(request):
    state = request.POST['state']
    data = State(state=state)
    data.save()
    return render(request, 'state.html')
def stateview(request):
    data = State.objects.all()
    return render(request, 'stateview.html',{'data':data})

# Terms Conditions

def termsconditions(request):
    return render(request,'termsconditions.html')

# Resort Image

def addimage(request):
    return render(request,'addimage.html')
def addimg(request):
    title=request.POST['title']
    photo = request.FILES['file']
    user = request.session['user']
    data=Image(title=title,photo=photo,username=user)
    data.save()
    return render(request,'addimage.html')
def viewimage(request):
    user = request.session['user']
    data= Image.objects.filter(username=user)
    return render(request,'viewimage.html',{'data':data})
def imagegallery(request):
    data = Image.objects.all()
    return render(request,'imagegallery.html',{'data':data})




def forgot(request):
    return render(request,'forgot.html')

def forgotpassword(request):
    return render(request,'forgot.html')
def save(request):
    return render(request, 'det1.html')
def add(request):
    return render(request,'add.html')
def det1(request):
    return render(request, 'det1.html')

#User payment
def pay(request):
    data = Booking.objects.all().last()
    data.status= request.POST['status']
    data.save()
    return render(request, 'userhome.html')
def payments(request):
    return render(request, 'payments.html')
def payment(request):
    user = request.session['user']
    data = Booking.objects.filter(username=user).last()
    data.status = request.POST['status']
    data.save()


    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_zQ1f5famQ1qxhU", "y7JUdHOOFHZhtoYEmkyMFYmK"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')
@csrf_exempt
def success(request):
    data = Booking.objects.all().last()
    data2 = User.objects.filter(username=data.username)
    return render(request, "success.html", {'data': data, 'data2': data2})
def base(request):

    return render(request, "base.html")
def index(request):
    return render(request, "index.html")


