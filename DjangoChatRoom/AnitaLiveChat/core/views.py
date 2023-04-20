from django.shortcuts import render, redirect
from .forms import SignUpForm
import maskpass
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

# Create your views here.
def frontPage(request):
    return render(request, 'core/frontPage.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials. Please try again or create an account.')
            return render(request, 'login.html', {'form': form, 'errors': {'username': ['User does not exist']}})
    else:
        return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #print("User signed up successfully!")
            return redirect('frontPage')
    else:
        form = SignUpForm()

    # Form is invalid, render signup page with error messages
    errors = form.errors.as_data()
    error_messages = {}
    for field, error_list in errors.items():
        error_messages[field] = [error.message for error in error_list]
    return render(request, 'core/signup.html', {'form':form, 'errors': error_messages})