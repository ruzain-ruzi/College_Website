from django.db import models


class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)


class staff(models.Model):
    staff_id = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()


class course(models.Model):
    course_name = models.CharField(max_length=200)


class subject(models.Model):
    subject_name = models.CharField(max_length=200)
    semester = models.IntegerField()
    course_id = models.ForeignKey(course, default=1, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)


class student(models.Model):
    student_id = models.ForeignKey(login, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    batch = models.BigIntegerField()
    course_id = models.ForeignKey(course, default=1, on_delete=models.CASCADE)


class student_feedback(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=350)
    date = models.DateField()


class staff_feedback(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=350)
    date = models.DateField()


class subject_attendance(models.Model):
    subject_id = models.ForeignKey(subject, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    batch = models.BigIntegerField()


class student_attendance(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    subject_attendance_id = models.ForeignKey(subject_attendance, on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=200)


class staff_leave_report(models.Model):
    subject_id = models.ForeignKey(subject, default=1, on_delete=models.CASCADE)
    reason = models.CharField(max_length=350)
    status = models.CharField(max_length=200)
    date = models.DateField()


class student_leave_report(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=350)
    date = models.DateField()


class student_mark(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject, on_delete=models.CASCADE)
    exam_marks = models.BigIntegerField()
    assignment_marks = models.BigIntegerField()

