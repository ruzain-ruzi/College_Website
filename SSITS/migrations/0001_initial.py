# Generated by Django 3.2.16 on 2022-12-14 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('staff_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SSITS.login')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('batch', models.BigIntegerField()),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SSITS.course')),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('semester', models.IntegerField()),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SSITS.course')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.staff')),
            ],
        ),
        migrations.CreateModel(
            name='subject_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('batch', models.BigIntegerField()),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.subject')),
            ],
        ),
        migrations.CreateModel(
            name='student_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_marks', models.BigIntegerField()),
                ('assignment_marks', models.BigIntegerField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.subject')),
            ],
        ),
        migrations.CreateModel(
            name='student_leave_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=350)),
                ('date', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.student')),
            ],
        ),
        migrations.CreateModel(
            name='student_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=350)),
                ('date', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.student')),
            ],
        ),
        migrations.CreateModel(
            name='student_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_status', models.CharField(max_length=200)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.student')),
                ('subject_attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.subject_attendance')),
            ],
        ),
        migrations.CreateModel(
            name='staff_leave_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=350)),
                ('status', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.staff')),
            ],
        ),
        migrations.CreateModel(
            name='staff_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=350)),
                ('date', models.DateField()),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSITS.staff')),
            ],
        ),
    ]