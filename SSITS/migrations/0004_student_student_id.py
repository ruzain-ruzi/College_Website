# Generated by Django 3.2.16 on 2022-12-19 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SSITS', '0003_rename_student_result_student_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SSITS.login'),
        ),
    ]
