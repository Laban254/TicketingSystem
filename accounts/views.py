# views.py

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model

User = get_user_model()

from django.shortcuts import render, redirect
from .forms import UserForm


from django.core.mail import send_mail
from .forms import UserForm

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']
            if role == 'customer':
                user.is_customer = True
                user.is_engineer = False
            elif role == 'support':
                user.is_customer = False
                user.is_engineer = True
            
            # Save user and set password
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Send email to user with their credentials
            send_user_credentials_email(user.email, form.cleaned_data['password'])

            messages.success(request, 'User created successfully!')
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Failed to create user. Please correct the errors.')
    else:
        form = UserForm()
    
    return render(request, 'accounts/create_user.html', {'form': form})

def send_user_credentials_email(email, password):
    subject = 'Your Account Credentials'
    message = f'Hello,\n\nYour account has been created successfully.\n\nEmail: {email}\nPassword: {password}\n\nThank you!'
    from_email = 'labanrotich6544@gmail.com'  
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


from .forms import LoginForm
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=email, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, f"Welcome back, {user.email}!")
                return redirect('dashboard:dashboard')  # Replace 'dashboard' with your actual dashboard URL
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})








































# from django.shortcuts import render, redirect
# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
# from .forms import RegisterCustomerForm

# User = get_user_model()

# def register_customer(request):
#     if request.method == 'POST':
#         form = RegisterCustomerForm(request.POST)
#         if form.is_valid():
#             var = form.save(commit=False)
#             var.is_customer = True
#             var.username = var.email
#             var.save()
#             messages.success(request, 'Account created. Please login.')
#             return redirect('accounts:login')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"Error in {field}: {error}")
#             return redirect('accounts:register_customer')
#     else:
#         form = RegisterCustomerForm()
#         context = {'form': form}
#         return render(request, 'accounts/register_customer.html', context)
    
# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return redirect('accounts:login')
#     else:
#         return render(request, 'accounts/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Active session ended. Login to continue.')
    return redirect('accounts:login')

def homepage(request):
     # Add your logic here to render the homepage template
    return render(request, 'accounts/home.html')

# change password
# update profile