# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import RegisterForm, ProfileUpdateForm, CustomLoginForm
# from .models import CustomUser, Profile
# from django.contrib.auth import login, authenticate, logout
# from django.core.mail import send_mail
# import random

# # Global dict to store OTP (for demo purpose)
# otp_storage = {}

# def home(request):
#     return render(request, 'lms_app/home.html')

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             otp = random.randint(1000, 9999)
#             otp_storage[user.email] = otp
#             # Send OTP to email
#             send_mail('Your OTP', f'Your OTP is {otp}', 'your-email@gmail.com', [user.email])
#             request.session['user_data'] = {
#                 'username': user.username,
#                 'email': user.email,
#                 'mobile': user.mobile,
#                 'password': request.POST['password1'],
#             }
#             return redirect('otp_verify')
#     else:
#         form = RegisterForm()
#     return render(request, 'lms_app/register.html', {'form': form})

# def otp_verify(request):
#     if request.method == "POST":
#         entered_otp = request.POST.get('otp')
#         user_data = request.session.get('user_data')
#         if user_data and str(otp_storage.get(user_data['email'])) == entered_otp:
#             user = CustomUser.objects.create_user(
#                 username=user_data['username'],
#                 email=user_data['email'],
#                 mobile=user_data['mobile'],
#                 password=user_data['password']
#             )
#             Profile.objects.create(user=user)
#             messages.success(request, "Registered Successfully. Please login.")
#             return redirect('login')
#         else:
#             messages.error(request, "Invalid OTP")
#     return render(request, 'lms_app/otp_verify.html')

# def user_login(request):
#     if request.method == "POST":
#         form = CustomLoginForm(request, data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('profile')
#     else:
#         form = CustomLoginForm()
#     return render(request, 'lms_app/login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('home')

# def profile(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request, 'lms_app/profile.html', {'profile': profile})

# def update_profile(request):
#     profile = Profile.objects.get(user=request.user)
#     if request.method == "POST":
#         form = ProfileUpdateForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile Updated Successfully!")
#             return redirect('profile')
#     else:
#         form = ProfileUpdateForm(instance=profile)
#     return render(request, 'lms_app/update_profile.html', {'form': form})

# def change_password(request):
#     if request.method == "POST":
#         old_password = request.POST['old_password']
#         new_password = request.POST['new_password']
#         if request.user.check_password(old_password):
#             request.user.set_password(new_password)
#             request.user.save()
#             messages.success(request, "Password changed successfully!")
#             return redirect('login')
#         else:
#             messages.error(request, "Old password incorrect.")
#     return render(request, 'lms_app/change_password.html')

# def delete_account(request):
#     if request.method == "POST":
#         request.user.delete()
#         messages.success(request, "Account deleted successfully!")
#         return redirect('home')
#     return render(request, 'lms_app/delete_account.html')






from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm, CustomLoginForm
from .models import CustomUser, Profile
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
import random

# Global dict to store OTP (for demo purpose)
otp_storage = {}

def home(request):
    return render(request, 'lms_app/home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            otp = random.randint(1000, 9999)
            otp_storage[user.email] = otp
            # Send OTP to email
            send_mail('Your OTP', f'Your OTP is {otp}', 'your-email@gmail.com', [user.email])
            request.session['user_data'] = {
                'username': user.username,
                'email': user.email,
                'mobile': user.mobile,
                'password': request.POST['password1'],
            }
            return redirect('otp_verify')
    else:
        form = RegisterForm()
    return render(request, 'lms_app/register.html', {'form': form})

def otp_verify(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        user_data = request.session.get('user_data')
        if user_data and str(otp_storage.get(user_data['email'])) == entered_otp:
            user = CustomUser.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                mobile=user_data['mobile'],
                password=user_data['password']
            )
            Profile.objects.create(user=user)
            messages.success(request, "Registered Successfully. Please login.")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP")
    return render(request, 'lms_app/otp_verify.html')

def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  # Redirecting to dashboard after login
    else:
        form = CustomLoginForm()
    return render(request, 'lms_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'lms_app/profile.html', {'profile': profile})

def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'lms_app/update_profile.html', {'form': form})

def change_password(request):
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        if request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password changed successfully!")
            return redirect('login')
        else:
            messages.error(request, "Old password incorrect.")
    return render(request, 'lms_app/change_password.html')

def delete_account(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Account deleted successfully!")
        return redirect('home')
    return render(request, 'lms_app/delete_account.html')

# Dashboard view
def dashboard(request):
    return render(request, 'lms_app/dashboard_with_charts.html')
