import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from SSITS.models import *


def student_home(request):
    return render(request, 'Student/index_student.html')


def view_attendance(request):
    student_attendance_db = student_attendance.objects.filter(student_id__student_id=5)
    return render(request, 'Student/view_attendance.html', {'attendance': student_attendance_db})


def apply_leave(request):
    if request.method == 'POST':
        sid = request.session['lid']
        reason = request.POST['reason']
        leave_date = request.POST['leave_date']

        student_db = student.objects.get(student_id=sid)

        leave_db = student_leave_report()
        leave_db.reason = reason
        leave_db.date = leave_date
        leave_db.student_id_id = student_db.id
        leave_db.save()

        messages.success(request, "Leave Applied")
        return redirect('/apply_leave')
    else:
        return render(request, 'Student/apply_leave.html')


def view_mark(request):
    sid = request.session['lid']
    mark_db = student_mark.objects.filter(student_id__student_id=sid)
    return render(request, 'Student/view_mark.html', {'mark': mark_db})


def send_feedback(request):
    if request.method == 'POST':
        sid = request.session['lid']
        feedback = request.POST['feedback']
        feedback_date = datetime.datetime.now()

        student_db = student.objects.get(student_id=sid)

        feedback_db = student_feedback()
        feedback_db.feedback = feedback
        feedback_db.student_id_id = student_db.student_id_id
        feedback_db.date = feedback_date
        feedback_db.save()

        messages.success(request, "Feedback Send")
        return redirect('/student_send_feedback')
    else:
        return render(request, 'Student/send_feedback.html')


def student_view_profile(request):
    sid = request.session['lid']
    student_db = student.objects.get(student_id=sid)

    return render(request, 'Student/view_profile.html', {'student': student_db})


def student_update_profile(request):
    sid = request.session['lid']
    if request.method == 'POST':
        name = request.POST['name']
        pict = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ruzai\PycharmProjects\College_Website\SSITS\static\pic\student\\" + date + '.jpg', pict)
        path = "/static/pic/student/" + date + '.jpg'
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        login_db = login.objects.filter(id=sid)
        login_db.update(username=email)

        student_db = student.objects.filter(student_id=sid)
        student_db.update(student_name=name)
        student_db.update(photo=path)
        student_db.update(gender=gender)
        student_db.update(email=email)
        student_db.update(phone_number=phone_number)

        messages.success(request, "Profile Updated")
        return redirect('/student_view_profile')
    else:
        student_db = student.objects.get(student_id=sid)
        return render(request, 'Student/update_profile.html', {'student': student_db})


def change_password(request):
    if request.method == 'POST':
        sid = request.session['lid']
        db = login.objects.get(id=sid)

        oldpasswd = request.POST['old_password']
        newpasswd = request.POST['new_password']
        conpasswd = request.POST['confirm_password']

        if db.password != oldpasswd:
            messages.error(request, "Incorrect Password")
            return redirect('/student_change_password')

        elif newpasswd != conpasswd:
            messages.error(request, "Password Mismatch")
            return redirect('/student_change_password')

        else:
            login_db = login.objects.filter(id=sid)
            login_db.update(password=newpasswd)

            messages.success(request, "Password Changed")
            return redirect('/student_view_profile')
    else:
        return render(request, 'Student/change_password.html')
