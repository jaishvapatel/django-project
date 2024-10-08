# Generated by Django 4.0 on 2023-09-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
        ('users', '0001_initial'),
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyAccessUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.customuser',),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject_specialization',
            field=models.ManyToManyField(blank=True, to='academic.Subject'),
        ),
        migrations.AddField(
            model_name='subjectallocation',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.academicyear'),
        ),
        migrations.AddField(
            model_name='subjectallocation',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='academic.classroom'),
        ),
        migrations.AddField(
            model_name='subjectallocation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocated_subjects', to='academic.subject'),
        ),
        migrations.AddField(
            model_name='subjectallocation',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.teacher'),
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(blank=True, help_text='the department associated with this subject', null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.department'),
        ),
        migrations.AddField(
            model_name='studentspreviousacademichistory',
            name='students_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='studentsmedicalhistory',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='studenthealthrecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='studentfile',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.academicyear'),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_student', to='academic.classroom'),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='academic.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='class_of_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.classyear'),
        ),
        migrations.AddField(
            model_name='student',
            name='grade_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.gradelevel'),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_guardian',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='academic.parent'),
        ),
        migrations.AddField(
            model_name='student',
            name='reason_left',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.reasonleft'),
        ),
        migrations.AddField(
            model_name='student',
            name='siblings',
            field=models.ManyToManyField(blank=True, to='academic.Student'),
        ),
        migrations.AddField(
            model_name='result',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.academicyear'),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='marksmanagement',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks_entered', to='academic.teacher'),
        ),
        migrations.AddField(
            model_name='marksmanagement',
            name='exam_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_marks', to='academic.examinationlisthandler'),
        ),
        migrations.AddField(
            model_name='marksmanagement',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_marks', to='academic.studentclass'),
        ),
        migrations.AddField(
            model_name='marksmanagement',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_marks', to='academic.subject'),
        ),
        migrations.AddField(
            model_name='gradescalerule',
            name='grade_scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.gradescale'),
        ),
        migrations.AddField(
            model_name='examinationlisthandler',
            name='classrooms',
            field=models.ManyToManyField(related_name='class_exams', to='academic.ClassRoom'),
        ),
        migrations.AddField(
            model_name='examinationlisthandler',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.teacher'),
        ),
        migrations.AddField(
            model_name='dormitoryallocation',
            name='dormitory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.dormitory'),
        ),
        migrations.AddField(
            model_name='dormitoryallocation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='dormitory',
            name='captain',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='academic.student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='class_teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='academic.teacher'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='grade_level',
            field=models.ForeignKey(blank=True, help_text="the grade level of the class ie: 'form one is in Grade one' ", null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.gradelevel'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_level', to='academic.classlevel'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='stream',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_stream', to='academic.stream'),
        ),
        migrations.AlterUniqueTogether(
            name='gradescalerule',
            unique_together={('min_grade', 'max_grade', 'grade_scale')},
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together={('name', 'stream')},
        ),
    ]
