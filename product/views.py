from django.shortcuts import render,redirect
from django.db.models import Q
from product.models import Users,Product
# forms
from product.forms import ProductForm,UsersForm
# filter
from django.db.models import Q
# decorator
from product.decorator import if_logedin,if_not_logedin
from django.views.decorators.cache import never_cache

@never_cache
@if_logedin
def login(request):
    
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        
        if Users.objects.filter(Q(email=user)| Q(mobile=user) & Q(password=password)).exists():
            request.session['id'] = True
            return redirect('home')
    return render(request,'login.html')

@never_cache
@if_logedin
def register(request):
    form = UsersForm()
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':form,
        'register':True,
    }
    return render(request,'users/add_user.html',context)
    
def logout(request):
    del request.session['id']
    return redirect('login')
#########################################################################3
@if_not_logedin  
@never_cache
def home(request):
    
    users = Users.objects.all()

    
    context = {
        'users': users,
        'products': products,
    }
    return render(request,'index.html',context)
##########################################################################
@if_not_logedin 
@never_cache
def add_users(request):
    form = UsersForm()
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
        'add':True,
    }
    return render(request,'users/add_user.html',context)
    
@never_cache
@if_not_logedin 
def edit_user(request,id):
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return redirect('home')
    form = UsersForm(instance=user)
    if request.method == 'POST':
        form = UsersForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
        'update':True
    }       
    return render(request,'users/add_user.html',context)
    
#########################################################################
@never_cache
@if_not_logedin 
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context={
        'form':form,
        'add': True,
    }
    return render(request,'product/add_product.html',context)
    
@if_not_logedin 
@never_cache   
def products(request):
    products = Product.objects.all()
    reset = False
    if request.GET.get('params'):
        value = request.GET.get('params')
        products = Product.objects.filter(
            Q(product_name__icontains=value)|
            Q(rate__icontains=value)|
            Q(description__icontains=value)|
            Q(status__icontains=value))
        reset = True
        
    context = {
        'products':products,
        'reset':reset,
    }
    return render(request,'product/product_list.html',context)

@if_not_logedin 
@never_cache    
def edit_product(request,id):
    try:
        user = Product.objects.get(id=id)
    except Users.DoesNotExist:
        return redirect('home')
    form = ProductForm(instance=user)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form':form,
        'update':True
    }       
    return render(request,'product/add_product.html',context)

@if_not_logedin 
@never_cache
def status_change(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect('products')
        
    product.status = not product.status
    product.save()
    return redirect('products')

@if_not_logedin   
@never_cache 
def delete_product(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect('products')
    product.delete()
    return redirect('products')
    