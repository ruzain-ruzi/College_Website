from django.urls import path
from . import views, Admin_views, Staff_views, Student_views

urlpatterns = [

    # Login
    path('', views.landing_page),
    path('login', views.login_page),

    # Admin Module
    path('admin_home', Admin_views.admin_home),
    path('add_staff', Admin_views.add_staff),
    path('view_staff', Admin_views.view_staff),
    path('update_staff/<id>', Admin_views.update_staff),
    path('remove_staff/<id>', Admin_views.remove_staff),
    path('add_course', Admin_views.add_course),
    path('view_course', Admin_views.view_course),
    path('update_course/<id>', Admin_views.update_course),
    path('remove_course/<id>', Admin_views.remove_course),
    path('add_subject', Admin_views.add_subject),
    path('view_subject', Admin_views.view_subject),
    path('update_subject/<id>', Admin_views.update_subject),
    path('remove_subject/<id>', Admin_views.remove_subject),
    path('add_student', Admin_views.add_student),
    path('view_student', Admin_views.view_student),
    path('update_student/<id>', Admin_views.update_student),
    path('remove_student/<id>', Admin_views.remove_student),
    path('view_student', Admin_views.view_student),
    path('view_student_feedback', Admin_views.view_student_feedback),
    path('view_staff_feedback', Admin_views.view_staff_feedback),
    path('view_subject_attendance', Admin_views.view_subject_attendance),
    path('view_student_attendance', Admin_views.view_student_attendance),
    path('view_staff_leave_report', Admin_views.view_staff_leave_report),
    path('approve_staff_leave/<id>', Admin_views.approve_staff_leave),
    path('reject_staff_leave/<id>', Admin_views.reject_staff_leave),

    # Staff Module
    path('staff_home', Staff_views.staff_home),
    path('view_allocated_subject', Staff_views.view_allocated_subject),
    path('mark_subject_attendance', Staff_views.mark_subject_attendance),
    path('mark_attendance/<id>', Staff_views.mark_attendance),
    path('take_student_attendance', Staff_views.take_student_attendance),
    path('student_present/<id>', Staff_views.student_present),
    path('student_absent/<id>', Staff_views.student_absent),
    path('view_student_mark', Staff_views.view_student_mark),
    path('add_mark', Staff_views.add_mark),
    path('add_student_mark/<id>', Staff_views.add_student_mark),
    path('update_mark', Staff_views.update_mark),
    path('update_student_mark/<id>', Staff_views.update_student_mark),
    path('apply_leave', Staff_views.apply_leave),
    path('staff_view_leave_report', Staff_views.staff_view_leave_report),
    path('send_feedback', Staff_views.send_feedback),
    path('view_profile', Staff_views.view_profile),
    path('update_profile', Staff_views.update_profile),
    path('change_password', Staff_views.change_password),

    # Student Module
    path('student_home', Student_views.student_home),
    path('view_attendance', Student_views.view_attendance),
    path('student_apply_leave', Student_views.apply_leave),
    path('view_mark', Student_views.view_mark),
    path('student_send_feedback', Student_views.send_feedback),
    path('student_view_profile', Student_views.student_view_profile),
    path('student_update_profile', Student_views.student_update_profile),
    path('student_change_password', Student_views.change_password),
]
