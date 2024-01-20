import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import logout , authenticate, login
from torch import StorageBase
from .models import StoreCategories, StoreProduct, UserModel 
from .forms import NewProductForm, NewCategoryForm, LoginForm, RegisterForm
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from .models import StoreCategories, StoreProduct
import pandas as pd

# Home page
def Home(request):
    context = {
        'title': 'Home',
        'products': StoreProduct.objects.all(),
        'categories': StoreCategories.objects.all(),
        
    }
    return render(request, 'index.html', {})


def Login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'Login.html', context)

def Register(request):
    context = {
        'title': 'Register',
        'LoginForm': LoginForm(),
        'RegisterForm': RegisterForm(),
    }
    return render(request, 'Register.html', context)

# Employee addition to the system
def Auth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        errors = []  
        message = []      
        
        if email == "" or email is None or email.isspace() or password == "" or password is None or password.isspace():
            errors.append("Email or Password is empty")
        
        print(email , password)
        LoggedUser = UserModel.objects.filter(email=email, password=password).first()
        
        print("Authenticated user:", LoggedUser)
        
        if LoggedUser is not None:
            login(request, LoggedUser)
            messages.success(request, "Logged in successfully")
            message.append("Logged in successfully")
            return JsonResponse({'success': True, 'message': message})
        else:
            errors.append("Invalid Credentials")
            return JsonResponse({'success': False, 'errors': errors})
    elif request.method == 'GET':
        errors.append("Invalid Request")
        return JsonResponse({'success': False, 'errors': errors})

    



# Employee Removal from the system
def UserDelete(request):
    # Collect enough info to identify employee
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = UserModel.objects.filter(email=email, password=password).first()

    # Delete employee if found
    if user:
        user.delete()

    # Return to home page
    return redirect('Home')


# Backend sign-in page for employees
def SignupHandler(request):
    if request.method == 'POST':
    
            email = request.POST.get('register-email')
            password = request.POST.get('register-password')
            errors = []
            messages = []
            
            # Perform registration some validation 
            
            print(email , password)
            
            if UserModel.objects.filter(email=email).exists():
                errors.append("Email already exists")
            
            
            if len(errors) > 0:
                return JsonResponse({'success': False , 'errors': errors})
            
            
            
        
            # Create new user
            User = UserModel.objects.create(
                email=email, 
                password=password,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
                )
            
            
            # Authenticate the user
            
            User = authenticate(request, email=email, password=password)
            messages.append("Logged in successfully")
            # Check if the user is authenticated
            
            if User is not None:
                login(request, User)
                messages.success(request, "Logged in successfully")
                return JsonResponse({'success': True , 'message': messages})
            else:
                # If user is not found, redirect to login page with an error message
                return JsonResponse({'success': False , 'errors': errors})


# Logout for everyone
def Logout(request):
    logout(request)
    return redirect('Home')

def AddProduct(request):
    if request.POST and request.FILES['file']:
        form = NewProductForm(request.POST)
        new_product = form.save(commit=False)
        FiletoUpload = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(FiletoUpload.name, FiletoUpload)
        firebase_Storage_URL = upload_to_firebase_storage(filename)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        new_product.image = firebase_Storage_URL
        new_product.save()
        
        form.save()
        return redirect('Administration')


# Ensure that the user has access before accessing the page
def Admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        context = {
            'title': 'Admin Panel',
            'users': UserModel.objects.all(),
            'products': StoreProduct.objects.all(),
            'ProductForm': NewProductForm(),
            'categories': StoreCategories.objects.all(),
        }
        return render(request, 'Admin.html', context)
    else:
        return HttpResponse("Access Denied")




# Function to upload images to firebase and return URL
def upload_to_firebase_storage(local_filename):
    # Upload the file to Firebase Storage and get the download URL
    bucket = StorageBase.bucket()
    blob = bucket.blob(local_filename)

    # Upload the file
    blob.upload_from_filename(local_filename)

    # Set the public URL of the file
    blob.make_public()

    # Get the download URL
    firebase_storage_url = blob.public_url

    return firebase_storage_url


# API Functions to retrieve data

def Api_Products_Info(request):
    
    if request.GET:
        
        products = StoreProduct.objects.all()

        # Create a list of products
        products_list = []
        for product in products:
            products_list.append({
                'name': product.name,
                'unique_id': product.unique_id,
                'stock': product.stock,
                'description': product.description,
                'sales': product.sales,
                'costPrice': product.costPrice,
                'price': product.price,
                'image': product.image,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
            })
        return JsonResponse({ 'products': products_list })
    elif request.POST:
        HttpResponse("POST");
        
        
def product_detail(request, product_name):
    product = get_object_or_404(StoreProduct, name=product_name)
    # Perform any additional logic you need with the product...
    return JsonResponse({'product_name': product.name, 'other_data': '...'})

