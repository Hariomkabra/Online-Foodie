from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Contact

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


def contact_view(request):
    if request.method == "POST":
        # Handle form submission, save data to Contact model
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phonenumber = request.POST.get('phonenumber')
        
        contact = Contact(name=name, email=email, desc=desc, phonenumber=phonenumber)
        contact.save()
        
        return render(request, 'contact_success.html')  # Assuming you have a success template
    
    return render(request, 'contact.html') 

def contact_success_view(request):
    return render(request, 'contact_success.html')