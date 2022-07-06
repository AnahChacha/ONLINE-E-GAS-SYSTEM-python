from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer,Product,Order
from django.db.models import Sum
from .forms import OrderForm,CustomerForm,ProductForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your v iews here.

#creating registerPage

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' +user)
            return redirect('loginPage')    
    
    context = {"form": form}
    return render(request,'customers/register.html' ,context) 

def logoutPage(request): 
    logout(request)
    return redirect('loginPage')

       


def home(request):
    customers=Customer.objects.all()
   # orders=customers.order_set.all()
    products=Product.objects.all()
    total_products=products.count()
    orders=Order.objects.all()
    total_order=orders.count()
    delivered=orders.filter(status ='Delivered').count()
    pending=orders.filter(status='Pending').count()
    print(pending)
    
    total_price=Product.objects.all().aggregate(Sum('price'))
    #total_price=Product.objects.annotate(Sum('price'))
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    context={"customers":customers,"products":products ,
    "total_products":total_products,"total_order":total_order,"pending":pending, "orders":orders,
    "delivered":delivered,"total_price":total_price}

    return render(request, 'customers/dashboard.html' ,context)

def products(request ):

    products=Product.objects.all()
    context={"products":products}
   
    return render(request, 'customers/product.html', context)



def customers(request ,pk):
    customers=Customer.objects.get(id=pk)
  
    orders=customers.order_set.all()
    total_orders=orders.count()
    context={"customers":customers,"orders":orders,"total_orders":total_orders}
    print(customers)

    return render(request, 'customers/customer.html' ,context)


    
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password =password);
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request, 'customers/login.html')



#creating order form
def createOrder_form(request):
    form=OrderForm()
    if request.method=="POST":
        print(request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

          


    context={"form":form}

    return render(request, 'customers/createOrder_form.html',context)



def updateOrder(request, pk):
    form=OrderForm()
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        form=OrderForm( request.POST ,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={"form":form}
  
    return render(request, 'customers/updateOrder_form.html',context)


def  deleteOrder(request, pk):
    order=Order.objects.get(id=pk)
    if request.method =="POST":
        order.delete()
        return redirect('home')
    
    context={"order": order}

    return render(request, 'customers/deleteOrder_form.html',context)


     



def createCustomer_form(request):
    form=CustomerForm()
    if request.method=="POST":
        print(request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

          

    context={"form":form}

    return render(request, 'customers/createCustomer_form.html',context)

def updateCustomer(request, pk):
  
    customer=Customer.objects.get(id=pk)
    form=CustomerForm(instance=customer)
    if request.method == 'POST':
        form=CustomerForm( request.POST ,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={"form":form ,'customer':customer}
  
    return render(request, 'customers/updateCustomer_form.html',context)




def createProduct_form(request):
    form=ProductForm()
    if request.method=="POST":
        print(request.POST)
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')

          

    context={"form":form}

    return render(request, 'customers/createProduct_form.html',context)

    
