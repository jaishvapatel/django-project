# Generated by Django 4.0 on 2023-09-27 14:46

import academic.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Class Level')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(blank=True, default=40, help_text='Enter total number of sits default is set to 25')),
                ('occupied_sits', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(help_text='Example 2020', max_length=100, unique=True)),
                ('full_name', models.CharField(blank=True, help_text='Example Class of 2020', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('order_rank', models.IntegerField(blank=True, help_text='Rank that courses will show up in reports', null=True)),
            ],
            options={
                'ordering': ('order_rank', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('occupied_beds', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DormitoryAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(auto_now_add=True)),
                ('date_till', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminationListHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('ends_date', models.DateField()),
                ('out_of', models.IntegerField()),
                ('comments', models.CharField(blank=True, help_text='Comments Regarding Exam', max_length=200, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Grade Level')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='GradeScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradeScaleRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('letter_grade', models.CharField(blank=True, max_length=50, null=True)),
                ('numeric_scale', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MarksManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_scored', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageToParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='this message will be shown to Parents when they log in')),
                ('start_date', models.DateField(default=django.utils.timezone.now, help_text='If blank the message will be posted starting today')),
                ('end_date', models.DateField(default=django.utils.timezone.now, help_text='if blank the message will end today')),
            ],
        ),
        migrations.CreateModel(
            name='MessageToTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='This message will be shown to teachers when they log in.')),
                ('start_date', models.DateField(default=django.utils.timezone.now, help_text='If blank the message will be posted starting today')),
                ('end_date', models.DateField(default=django.utils.timezone.now, help_text='if blank the message will end today')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=250, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=300, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=300, verbose_name='Last Name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('parent_type', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Guardian', 'Guardian')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(help_text='personal phone number', max_length=150)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, help_text='current occupation', max_length=255)),
                ('monthly_income', models.FloatField(blank=True, help_text='parents average monthly income')),
                ('single_parent', models.BooleanField(blank=True, default=False, help_text='is he/she a single parent')),
                ('alt_email', models.EmailField(blank=True, help_text='personal Email ', max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='Parent_images')),
                ('inactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReasonLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField(null=True)),
                ('cat_gpa', models.FloatField(null=True)),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three'), ('FOUR', 'Four')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[academic.validators.stream_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, null=True, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=150, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=150, null=True, verbose_name='Last Name')),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('date_dismissed', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('street', models.CharField(blank=True, max_length=255)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True)),
                ('admission_date', models.DateTimeField(auto_now_add=True)),
                ('admission_number', models.CharField(blank=True, max_length=50, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='StudentsImages')),
                ('cache_gpa', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='student_files')),
            ],
        ),
        migrations.CreateModel(
            name='StudentHealthRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentsMedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='students_medical_files')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsPreviousAcademicHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('former_school', models.CharField(help_text='Former school name', max_length=255)),
                ('last_gpa', models.FloatField()),
                ('notes', models.CharField(blank=True, help_text='Indicate students academic performance according to your observation', max_length=255)),
                ('academic_record', models.FileField(blank=True, upload_to='students_former_academic_files')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('subject_code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('is_selectable', models.BooleanField(default=False, help_text='select if subject is optional')),
                ('graded', models.BooleanField(default=True, help_text='Teachers can submit grades for this course')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three'), ('FOUR', 'Four')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=250, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=300, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=300, verbose_name='Last Name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('teacher_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('empId', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('tin_number', models.CharField(blank=True, max_length=9, null=True)),
                ('nssf_number', models.CharField(blank=True, max_length=9, null=True)),
                ('short_name', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('isTeacher', models.BooleanField(default=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=150)),
                ('alt_email', models.EmailField(blank=True, help_text='Personal Email apart from the one given by the school', max_length=254, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee_images')),
                ('inactive', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
            },
        ),
    ]
