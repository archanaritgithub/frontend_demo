from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages
from store.forms import CustomUserForm
from django import views

def register(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to continue")
            return redirect('login/')
    context = {'form':form}
    return render(request, 'apps/auth/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in ")
        return redirect('homee')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwrd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwrd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in sucessfully")
                return redirect('homee')
            else:
                messages.error(request, "invalid Username or Password")
                return redirect('/login')
        return render(request, 'apps/auth/login.html')
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out Successfully')
        return redirect('homee')
    