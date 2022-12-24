from django.contrib import messages
from django.shortcuts import render, redirect
from SSITS.models import *


def landing_page(request):
    return render(request, 'index.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        login_db = login.objects.filter(username=username, password=password)

        if login_db.exists():
            login_db = login_db[0]
            if login_db.user_type == 'admin':
                messages.success(request, "Login Successful")
                return redirect('/admin_home')
            elif login_db.user_type == 'staff':
                request.session['lid'] = login_db.id
                messages.success(request, "Login Successful")
                return redirect('/staff_home')
            elif login_db.user_type == 'student':
                request.session['lid'] = login_db.id
                messages.success(request, "Login Successful")
                return redirect('/student_home')
            else:
                messages.error(request, 'Incorrect Email ID/Password')
                return redirect('/login')
        else:
            messages.error(request, 'Incorrect Email ID/Password')
            return redirect('/login')
    else:
        return render(request, 'index.html')