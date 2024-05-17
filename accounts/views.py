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
            messages.success(request, 'Account created. Please login.')
            return redirect('accounts:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
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
            messages.error(request, 'Invalid username or password.')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Active session ended. Login to continue.')
    return redirect('accounts:login')

def homepage(request):
    # Add your logic here to render the homepage template
    return render(request, 'accounts/home.html')

# change password
# update profile