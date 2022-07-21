from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer,Product,Order
from django.db.models import *
from .models import *
from .forms import OrderForm,CustomerForm,ProductForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  .decorator import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

# Create your v iews here.

#creating registerPage

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account created successfully for ' +username)
            return redirect('loginPage')    
    
    context = {"form": form}
    return render(request,'customers/register.html' ,context) 

def logoutPage(request): 
    logout(request)
    return redirect('loginPage')

       

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['admin'])
@admin_only
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
    total_customers=customers.count()
    
    total_price=Product.objects.all().aggregate(Sum('price'))
    #total_price=Product.objects.annotate(Sum('price'))
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    context={"customers":customers,"products":products ,
    "total_products":total_products,"total_order":total_order,"pending":pending, "orders":orders,
    "delivered":delivered,"total_price":total_price,"total_customers":total_customers}

    return render(request, 'customers/dashboard.html' ,context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def products(request ):

    products=Product.objects.all()
    context={"products":products}

    return render(request, 'customers/product.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def customers(request ,pk):
    customers=Customer.objects.get(id=pk)
  
    orders=customers.order_set.all()
    total_orders=orders.count()
    context={"customers":customers,"orders":orders,"total_orders":total_orders}
    print(customers)

    return render(request, 'customers/customer.html' ,context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def customer(request):
    customer = Customer.objects.all()
    context={"customer":customer}

    return render(request, 'customers/customer.html' ,context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password =password);
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request, 'customers/login.html')

#test123@T7

#creating order form
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
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
def  deleteCustomer(request, pk):
    customer=Customer.objects.get(id=pk)
    if request.method =="POST":
        customer.delete()
        return redirect('home')
    
    context={"customer": customer}

    return render(request, 'customers/deleteCustomer.html',context)

def updateProducts(request, pk):
  
    product=Product.objects.get(id=pk)
    form=ProductForm(instance=product)
    if request.method == 'POST':
        form=ProductForm( request.POST ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')

    context={"form":form ,'product':product}
  
    return render(request, 'customers/createProduct_Form.html',context)

def deleteProduct(request,pk):

    product=Product.objects.get(id=pk)
    form=ProductForm(instance=product)
    if request.method == 'POST':
        form=ProductForm( request.POST ,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')

    context={"form":form ,'product':product}

    return render(request, 'customers/deleteProduct.html', context)

def userPage(request):
    return  render(request ,'customers/user.html')


