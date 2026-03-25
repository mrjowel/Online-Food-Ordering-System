from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Contact,Employees,product,Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        message= request.POST.get("message")

        obj = Contact(name=name, email=email, message=message)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"

    return render(request,'contact.html',context)
def crud(request):

    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return render(request,'crud.html', context)

def add_cart(request):
    return render(request, 'addtocart.html')

@login_required(login_url='login')
def HomePage(request):
    return render (request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dash')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def ShowAllProducts(request):
    products=product.objects.all()

    context = {
        'products':products
    }

    return render(request, 'showProducts.html',context)

def dashboard(request):
    return render(request,'dashboard.html')

def orderdet(request):
    context={}
    if request.method=="POST":
        uname= request.POST.get("username")
        phone= request.POST.get("phone")
        address= request.POST.get("address")
       
        if uname is not None:
            return redirect('payment')
        obj = Order(uname=uname, phone=phone, address=address)
        obj.save()
        context['message']=f"Dear {uname}, Thanks for your time!"
    
    return render(request,'form.html',context)
