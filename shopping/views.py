from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product

def login_view(request):
    # cred = {"user": None, "pass": None}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # cred.update({"user": username})
            # cred.update({"pass": password})
            login(request, user)
            # Redirect to a dashboard page after successful login
            return redirect('home')
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')


def index(request):
    return render(request, 'Home.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            # Redirect to a dashboard page after successful login
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to the home page or any other desired page
    return redirect('home')
    
    
def about(request):
    return render(request, 'Aboutus.html')
def contact(request):
    return render(request, 'Contactus.html')


# product upload
def shop(request):
    return render(request, 'Shop.html',{
        'products': Product.objects.all()
    })
    

def blogs(request):
    return render(request, 'Blogs.html')
def privacy(request):
    return render(request, 'privacy.html')
def terms(request):
    return render(request, 'terms.html')
def book(request):
    return render(request, 'bookings.html')
def order(request):
    return render(request, 'orders.html')
def services(request):
    # return render(request, 'terms.html')
    return render(request, 'cart.html')
def categories(request):
    # return render(request, 'terms.html')
    return redirect('home')