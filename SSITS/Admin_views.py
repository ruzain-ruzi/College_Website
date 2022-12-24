import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from SSITS.models import *


def admin_home(request):
    return render(request, 'Admin/index_admin.html')


def add_staff(request):
    if request.method == 'POST':
        name = request.POST['staff_name']
        pict = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ruzai\PycharmProjects\College_Website\SSITS\static\pic\staff\\" + date + '.jpg', pict)
        path = "/static/pic/staff/" + date + '.jpg'
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        login_db = login()
        login_db.username = email
        login_db.password = 'staff@ssitscollege'
        login_db.user_type = 'staff'
        login_db.save()

        staff_db = staff()
        staff_db.staff_name = name
        staff_db.photo = path
        staff_db.gender = gender
        staff_db.email = email
        staff_db.phone_number = phone_number
        staff_db.staff_id = login_db
        staff_db.save()

        messages.success(request, "Staff Added")
        return redirect('/view_staff')
    else:
        return render(request, 'Admin/add_staff.html')


def view_staff(request):
    staff_db = staff.objects.all()
    return render(request, 'Admin/view_staff.html', {'staff': staff_db})


def update_staff(request, id):
    if request.method == 'POST':
        name = request.POST['staff_name']
        pict = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ruzai\PycharmProjects\College_Website\SSITS\static\pic\staff\\" + date + '.jpg', pict)
        path = "/static/pic/staff/" + date + '.jpg'
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        login_db = login.objects.filter(id=id)
        login_db.update(username=email)

        staff_db = staff.objects.filter(staff_id=id)
        staff_db.update(staff_name=name)
        staff_db.update(photo=path)
        staff_db.update(gender=gender)
        staff_db.update(email=email)
        staff_db.update(phone_number=phone_number)

        messages.success(request, "Staff Updated")
        return redirect('/view_staff')
    else:
        staff_db = staff.objects.get(id=id)
        return render(request, 'Admin/update_staff.html', {'staff': staff_db})


def remove_staff(request, id):
    staff.objects.get(staff_id=id).delete()
    login.objects.get(id=id).delete()

    messages.success(request, "Staff Removed")
    return redirect('/view_staff')


def add_course(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']

        course_db = course()
        course_db.course_name = course_name
        course_db.save()

        messages.success(request, "Course Added")
        return redirect('/view_course')
    else:
        return render(request, 'Admin/add_course.html')


def view_course(request):
    course_db = course.objects.all()
    return render(request, 'Admin/view_course.html', {'course': course_db})


def update_course(request, id):
    if request.method == 'POST':
        course_name = request.POST['course_name']

        course_db = course.objects.filter(id=id)
        course_db.update(course_name=course_name)

        messages.success(request, "Course Updated")
        return redirect('/view_course')
    else:
        course_db = course.objects.get(id=id)
        return render(request, 'Admin/update_course.html', {'course': course_db})


def remove_course(request, id):
    course.objects.get(id=id).delete()

    messages.success(request, "Course Removed")
    return redirect('/view_course')


def add_subject(request):
    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        semester = request.POST['semester']
        course_name = request.POST['course']
        staff_name = request.POST['staff']

        course_db = course.objects.get(course_name=course_name)
        staff_db = staff.objects.get(staff_name=staff_name)

        subject_db = subject()
        subject_db.subject_name = subject_name
        subject_db.semester = semester
        subject_db.course_id_id = course_db.id
        subject_db.staff_id_id = staff_db.id
        subject_db.save()

        messages.success(request, "Subject Added")
        return redirect('/view_subject')
    else:
        course_db = course.objects.all()
        staff_db = staff.objects.all()
        return render(request, 'Admin/add_subject.html', {'course': course_db, 'staff': staff_db})


def view_subject(request):
    subject_db = subject.objects.all()

    return render(request, 'Admin/view_subject.html', {'subject': subject_db})


def update_subject(request, id):
    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        semester = request.POST['semester']
        course_name = request.POST['course']
        staff_name = request.POST['staff']

        course_db = course.objects.get(course_name=course_name)
        staff_db = staff.objects.get(staff_name=staff_name)

        subject_db = subject.objects.filter(id=id)
        subject_db.update(subject_name=subject_name)
        subject_db.update(semester=semester)

        messages.success(request, "Subject Updated")
        return redirect('/view_subject')
    else:
        subject_db = subject.objects.get(id=id)
        course_db = course.objects.all()
        staff_db = staff.objects.all()
        return render(request, 'Admin/update_subject.html',
            {'subject': subject_db, 'course': course_db, 'staff': staff_db})


def remove_subject(request, id):
    subject.objects.get(id=id).delete()

    messages.success(request, "Subject Removed")
    return redirect('/view_subject')


def add_student(request):
    if request.method == 'POST':
        name = request.POST['student_name']
        pict = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ruzai\PycharmProjects\College_Website\SSITS\static\pic\student\\" + date + '.jpg', pict)
        path = "/static/pic/student/" + date + '.jpg'
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        course_name = request.POST['course']
        batch = request.POST['batch']

        course_db = course.objects.get(course_name=course_name)

        login_db = login()
        login_db.username = email
        login_db.password = 'student@ssitscollege'
        login_db.user_type = 'student'
        login_db.save()

        student_db = student()
        student_db.student_name = name
        student_db.photo = path
        student_db.gender = gender
        student_db.email = email
        student_db.phone_number = phone_number
        student_db.course_id_id = course_db.id
        student_db.batch = batch
        student_db.student_id = login_db
        student_db.save()

        messages.success(request, "Student Added")
        return redirect('/view_student')
    else:
        course_db = course.objects.all()
        return render(request, 'Admin/add_student.html', {'course': course_db})


def view_student(request):
    student_db = student.objects.all()
    return render(request, 'Admin/view_student.html', {'student': student_db})


def update_student(request, id):
    if request.method == 'POST':
        name = request.POST['student_name']
        pict = request.FILES['photo']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ruzai\PycharmProjects\College_Website\SSITS\static\pic\student\\" + date + '.jpg', pict)
        path = "/static/pic/student/" + date + '.jpg'
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        course_name = request.POST['course']
        batch = request.POST['batch']

        student_db = student.objects.filter(id=id)
        student_db.update(student_name=name)
        student_db.update(photo=path)
        student_db.update(gender=gender)
        student_db.update(email=email)
        student_db.update(phone_number=phone_number)
        student_db.update(batch=batch)

        messages.success(request, "Student Updated")
        return redirect('/view_student')
    else:
        student_db = student.objects.get(id=id)
        course_db = course.objects.all()
        return render(request, 'Admin/update_student.html', {'student': student_db, 'course': course_db})


def remove_student(request, id):
    student.objects.get(id=id).delete()

    messages.success(request, "Student Removed")
    return redirect('/view_student')


def view_student_feedback(request):
    stud_feedback_db = student_feedback.objects.all()
    return render(request, 'Admin/view_student_feedback.html', {'feedback': stud_feedback_db})


def view_staff_feedback(request):
    staff_feedback_db = staff_feedback.objects.all()
    return render(request, 'Admin/view_staff_feedback.html', {'feedback': staff_feedback_db})


def view_subject_attendance(request):
    sub_attendance_db = subject_attendance.objects.all()
    return render(request, 'Admin/view_subject_attendance.html', {'attendance': sub_attendance_db})


def view_student_attendance(request):
    stud_attendance_db = student_attendance.objects.all()
    return render(request, 'Admin/view_student_attendance.html', {'attendance': stud_attendance_db})


def view_staff_leave_report(request):
    staff_leave_db = staff_leave_report.objects.all()
    return render(request, 'Admin/view_staff_leave_report.html', {'leave': staff_leave_db})


def approve_staff_leave(request, id):
    staff_leave_db = staff_leave_report.objects.filter(id=id)
    staff_leave_db.update(status='approved')

    messages.success(request, "Leave Approved")
    return redirect('/view_staff_leave_report')


def reject_staff_leave(request, id):
    staff_leave_db = staff_leave_report.objects.filter(id=id)
    staff_leave_db.update(status='rejected')

    messages.success(request, "Leave Rejected")
    return redirect('/view_staff_leave_report')