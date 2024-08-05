from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def admin_page(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            reg_form = RegistrationForm(request.POST)
            if reg_form.is_valid():
                user = reg_form.save()
                messages.success(request, 'Registrasi berhasil!')
            else:
                error_messages = ['Registrasi gagal. Silakan periksa kesalahan di bawah:']
                for field, errors in reg_form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field}: {error}")
                
                messages.error(request, "\n".join(error_messages))
            return redirect('admin_page')

        elif 'login' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                if user.is_admin():
                    messages.success(request, 'Login berhasil!')
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, 'Login gagal. Akses tidak diizinkan.')
            else:
                error_messages = ['Login gagal. Silakan periksa kesalahan di bawah:']
                for field, errors in login_form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field}: {error}")
                
                messages.error(request, "\n".join(error_messages))
            return redirect('admin_page')

    else:
        reg_form = RegistrationForm()
        reg_form.fields['role'].initial = 'admin'
        login_form = LoginForm()

    return render(request, 'main/admin_page.html', {
        'reg_form': reg_form,
        'login_form': login_form
    })

def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')

def dokter_page(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            reg_form = RegistrationForm(request.POST)
            if reg_form.is_valid():
                user = reg_form.save()
                messages.success(request, 'Registrasi berhasil!')
            else:
                error_messages = ['Registrasi gagal. Silakan periksa kesalahan di bawah:']
                for field, errors in reg_form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field}: {error}")
                
                messages.error(request, "\n".join(error_messages))
            return redirect('dokter_page')

        elif 'login' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                if user.is_dokter():
                    messages.success(request, 'Login berhasil!')
                    return redirect('dokter_dashboard')
                else:
                    messages.error(request, 'Login gagal. Akses tidak diizinkan.')
            else:
                error_messages = ['Login gagal. Silakan periksa kesalahan di bawah:']
                for field, errors in login_form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field}: {error}")
                
                messages.error(request, "\n".join(error_messages))
            return redirect('dokter_page')

    else:
        reg_form = RegistrationForm()
        reg_form.fields['role'].initial = 'dokter'
        login_form = LoginForm()

    return render(request, 'main/dokter_page.html', {
        'reg_form': reg_form,
        'login_form': login_form
    })

def dokter_dashboard(request):
    return render(request, 'main/dokter_dashboard.html')

def pasien_page(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            reg_form = RegistrationForm(request.POST)
            if reg_form.is_valid():
                user = reg_form.save()
                messages.success(request, 'Registrasi berhasil!')
            else:
                error_messages = ['Registrasi gagal. Silakan periksa kesalahan di bawah:']
                for field, errors in reg_form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field}: {error}")
                
                messages.error(request, "\n".join(error_messages))
            return redirect('pasien_page')

        elif 'login' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                if user.is_dokter():
                    messages.success(request, 'Login berhasil!')
                    return redirect('pasien_dashboard')
                else:
                    messages.error(request, 'Login gagal. Akses tidak diizinkan.')
            else:
                error_messages = ['Login gagal. Silakan periksa kesalahan di bawah:']
                for field, errors in login_form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field}: {error}")
                
                messages.error(request, "\n".join(error_messages))
            return redirect('pasien_page')

    else:
        reg_form = RegistrationForm()
        reg_form.fields['role'].initial = 'pasien'
        login_form = LoginForm()

    return render(request, 'main/pasien_page.html', {
        'reg_form': reg_form,
        'login_form': login_form
    })

def pasien_dashboard(request):
    return render(request, 'main/pasien_dashboard.html')

def logout_view(request):
    auth_logout(request)
    messages.info(request, 'Anda telah berhasil logout.')
    return redirect('home') 
