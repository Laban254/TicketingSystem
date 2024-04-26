from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import RegisterCustomerForm

User = get_user_model()

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.save()
            messages.success(request, 'account created, please login')
            return redirect('accounts:login')
        else:
            messages.warning(request, 'something went wrong, please check form errors')
            return redirect('accounts:register_customer')
    else:
        form = RegisterCustomerForm()
        context = {'form': form}
        return render(request, 'accounts/register_customer.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong, please check for errors')
            return redirect('accounts:login')
        

    else:
        return render(request, 'accounts/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Active session ended. login to continue')
    return redirect('accounts:login')

def homepage(request):
    # Add your logic here to render the homepage template
    return render(request, 'accounts/home.html')

# change password
# update profile