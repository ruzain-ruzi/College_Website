import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from SSITS.models import *


def staff_home(request):
    return render(request, 'Staff/index_staff.html')


def view_allocated_subject(request):
    sid = request.session['lid']
    subject_db = subject.objects.filter(staff_id__staff_id=sid)
    return render(request, 'Staff/subject_allocated.html', {'subject': subject_db})


def mark_subject_attendance(request):
    sid = request.session['lid']
    subject_db = subject.objects.filter(staff_id__staff_id=sid)

    sfilter = request.GET.get('sfilter')
    if sfilter:
        subject_filter = subject.objects.filter(subject_name=sfilter)
        if subject_filter:
            return render(request, 'Staff/subject_attendance.html',
                          {'subject': subject_filter, 'subj': subject_db})

    return render(request, 'Staff/subject_attendance.html', {'subject': subject_db, 'subj': subject_db})


def mark_attendance(request, id):
    subject_db = subject.objects.get(id=id)
    attendance_date = datetime.datetime.now()

    attendance_db = subject_attendance()
    attendance_db.attendance_date = attendance_date
    attendance_db.batch = 2021
    attendance_db.subject_id_id = subject_db.id
    attendance_db.save()

    messages.success(request, "Attendance Marked")
    return redirect('/mark_subject_attendance')


def take_student_attendance(request):
    sid = request.session['lid']
    subject_db = subject.objects.filter(staff_id__staff_id=sid)
    subject_db = subject_db[0]
    student_db = student.objects.filter(course_id=subject_db.course_id)
    subj = subject.objects.filter(staff_id__staff_id=sid)

    sfilter = request.GET.get('sfilter')
    bfilter = request.GET.get('bfilter')
    if sfilter:
        subj_filter = subject.objects.get(subject_name=sfilter)
        subject_filter = student_db.filter(course_id__course_name=subj_filter.course_id.course_name)
        if subject_filter:
            return render(request, 'Staff/student_attendance.html',
                          {'student': subject_filter, 'stud': student_db, 'subject': subj})
    elif bfilter:
        batch_filter = student_db.filter(batch=bfilter)
        if batch_filter:
            return render(request, 'Staff/student_attendance.html',
                          {'student': batch_filter, 'stud': student_db, 'subject': subj})

    return render(request, 'Staff/student_attendance.html', {'student': student_db, 'stud': student_db, 'subject': subj})


def student_present(request, id):
    sid = request.session['lid']
    subject_attendance_db = subject_attendance.objects.get(subject_id__staff_id__staff_id=sid)

    attendance_db = student_attendance()
    attendance_db.attendance_status = 'present'
    attendance_db.student_id_id = id
    attendance_db.subject_attendance_id_id = subject_attendance_db.id
    attendance_db.save()

    messages.success(request, "Marked Present")
    return redirect('/take_student_attendance')


def student_absent(request, id):
    sid = request.session['lid']
    subject_attendance_db = subject_attendance.objects.get(subject_id__staff_id__staff_id=sid)

    attendance_db = student_attendance()
    attendance_db.attendance_status = 'absent'
    attendance_db.student_id_id = id
    attendance_db.subject_attendance_id_id = subject_attendance_db.id
    attendance_db.save()

    messages.success(request, "Marked Absent")
    return redirect('/take_student_attendance')


def view_student_mark(request):
    sid = request.session['lid']
    student_mark_db = student_mark.objects.filter(subject_id__staff_id__staff_id=sid)
    return render(request, 'Staff/view_student_mark.html', {'mark': student_mark_db})


def add_mark(request):
    sid = request.session['lid']
    subject_db = subject.objects.get(staff_id__staff_id=sid)
    student_db = student.objects.filter(course_id=subject_db.course_id)
    return render(request, 'Staff/add_student_mark.html', {'student': student_db})


def add_student_mark(request, id):
    sid = request.session['lid']
    if request.method == 'POST':
        assignment_mark = request.POST['assignment']
        exam_mark = request.POST['exam']

        subject_db = subject.objects.get(staff_id__staff_id=sid)
        student_db = student.objects.get(id=id)
        student_mark_db = student_mark.objects.filter(student_id=student_db.id)

        if student_mark_db.exists():
            messages.success(request, "Already Added")
            return redirect('/update_student_mark')
        else:
            student_mark_db = student_mark()
            student_mark_db.assignment_marks = assignment_mark
            student_mark_db.exam_marks = exam_mark
            student_mark_db.student_id_id = student_db.id
            student_mark_db.subject_id_id = subject_db.id
            student_mark_db.save()

        messages.success(request, "Mark Added")
        return redirect('/view_student_mark')
    else:
        subject_db = subject.objects.get(staff_id__staff_id=sid)
        student_db = student.objects.filter(course_id=subject_db.course_id)
        return render(request, 'Staff/add_student_mark.html', {'student': student_db})


def update_mark(request):
    sid = request.session['lid']
    student_mark_db = student_mark.objects.filter(subject_id__staff_id__staff_id=sid)
    return render(request, 'Staff/update_student_mark.html', {'student_mark': student_mark_db})


def update_student_mark(request, id):
    sid = request.session['lid']
    if request.method == 'POST':
        assignment_mark = request.POST['assignment']
        exam_mark = request.POST['exam']

        student_mark_db = student_mark.objects.filter(id=id)
        student_mark_db.update(assignment_marks=assignment_mark)
        student_mark_db.update(exam_marks=exam_mark)

        messages.success(request, "Mark Updated")
        return redirect('/view_student_mark')
    else:
        student_mark_db = student_mark.objects.filter(subject_id__staff_id__staff_id=sid)
        return render(request, 'Staff/update_student_mark.html', {'student_mark': student_mark_db})


def apply_leave(request):
    if request.method == 'POST':
        sid = request.session['lid']
        reason = request.POST['reason']
        leave_date = request.POST['leave_date']

        subject_db = subject.objects.get(staff_id__staff_id=sid)

        leave_db = staff_leave_report()
        leave_db.reason = reason
        leave_db.date = leave_date
        leave_db.status = 'pending'
        leave_db.subject_id_id = subject_db.id
        leave_db.save()

        messages.success(request, "Leave Applied")
        return redirect('/apply_leave')
    else:
        return render(request, 'Staff/apply_leave.html')


def staff_view_leave_report(request):
    sid = request.session['lid']
    staff_leave_db = staff_leave_report.objects.filter(subject_id__staff_id__staff_id=sid)

    return render(request, 'Staff/view_leave_report.html', {'leave': staff_leave_db})


def send_feedback(request):
    if request.method == 'POST':
        sid = request.session['lid']

        feedback = request.POST['feedback']
        feedback_date = datetime.datetime.now()

        subject_db = subject.objects.get(staff_id__staff_id=sid)

        feedback_db = staff_feedback()
        feedback_db.feedback = feedback
        feedback_db.staff_id_id = subject_db.staff_id_id
        feedback_db.date = feedback_date
        feedback_db.save()

        messages.success(request, "Feedback Send")
        return redirect('/send_feedback')
    else:
        return render(request, 'Staff/send_feedback.html')


def view_profile(request):
    sid = request.session['lid']
    staff_db = staff.objects.get(staff_id=sid)

    return render(request, 'Staff/view_profile.html', {'staff': staff_db})


def update_profile(request):
    sid = request.session['lid']
    if request.method == 'POST':
        name = request.POST['name']
        pict = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ruzai\PycharmProjects\College_Website\SSITS\static\pic\staff\\" + date + '.jpg', pict)
        path = "/static/pic/staff/" + date + '.jpg'
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        login_db = login.objects.filter(id=sid)
        login_db.update(username=email)

        staff_db = staff.objects.filter(staff_id=sid)
        staff_db.update(staff_name=name)
        staff_db.update(photo=path)
        staff_db.update(gender=gender)
        staff_db.update(email=email)
        staff_db.update(phone_number=phone_number)

        messages.success(request, "Profile Updated")
        return redirect('/view_profile')
    else:
        staff_db = staff.objects.get(staff_id=sid)
        return render(request, 'Staff/update_profile.html', {'staff': staff_db})


def change_password(request):
    if request.method == 'POST':
        sid = request.session['lid']

        db = login.objects.get(id=sid)

        oldpasswd = request.POST['old_password']
        newpasswd = request.POST['new_password']
        conpasswd = request.POST['confirm_password']

        if db.password != oldpasswd:
            messages.error(request, "Incorrect Password")
            return redirect('/change_password')

        elif newpasswd != conpasswd:
            messages.error(request, "Password Mismatch")
            return redirect('/change_password')

        else:
            login_db = login.objects.filter(id=sid)
            login_db.update(password=newpasswd)

            messages.success(request, "Password Changed")
            return redirect('/view_profile')
    else:
        return render(request, 'Staff/change_password.html')
