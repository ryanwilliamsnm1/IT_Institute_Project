# Generated by Django 5.1.4 on 2024-12-07 04:42

import django.core.validators
import django.db.models.deletion
import institute_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Info_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('surname', models.CharField(blank=True, max_length=20, null=True, verbose_name='Surname')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField()),
                ('image', models.ImageField(default=None, null=True, upload_to='images')),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
        migrations.CreateModel(
            name='Student_Course_Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_type', models.CharField(choices=[('Select', 'select'), ('Online', 'online'), ('Offline', 'offline')], default=[('Select', 'select'), ('Python', 'Python'), ('Digital Marketing', 'Digital Marketing'), ('Software Testing', 'Software Testing')], max_length=100)),
                ('course', models.CharField(choices=[('Select', 'select'), ('Python', 'Python'), ('Digital Marketing', 'Digital Marketing'), ('Software Testing', 'Software Testing')], default=[('Select', 'select'), ('Online', 'online'), ('Offline', 'offline')], max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_app.student_info_model')),
            ],
            options={
                'db_table': 'Course_details',
            },
        ),
        migrations.CreateModel(
            name='Student_Contact_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=250, verbose_name='Email Id')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20, validators=[institute_app.validators.validate_postal_code], verbose_name='Postal Code')),
                ('mobile_num', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Mobile number must be entered in the format: '9999999999' or '+919999999999'.", regex='^\\+91[789]\\d{9}$|^[789]\\d{9}$')])),
                ('aadhaar_number', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute_app.student_info_model')),
            ],
            options={
                'db_table': 'student_contact',
            },
        ),
    ]
