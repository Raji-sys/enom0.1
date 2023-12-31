# Generated by Django 4.1.7 on 2023-07-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_personaldetail_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='qualification',
        ),
        migrations.AlterField(
            model_name='governmentappointment',
            name='grade_level',
            field=models.CharField(blank=True, choices=[('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='governmentappointment',
            name='salary_scale',
            field=models.CharField(blank=True, choices=[('CONHESS', 'CONHESS'), ('CONMESS', 'CONMESS'), ('GIPMIS', 'GIPMIS')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='governmentappointment',
            name='type_of_appointment',
            field=models.CharField(blank=True, choices=[('CASUAL', 'CASUAL'), ('LOCUM', 'LOCUM'), ('PERMANENT', 'PERMANENT'), ('PROBATION', 'PROBATION')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='governmentappointment',
            name='type_of_cadre',
            field=models.CharField(blank=True, choices=[('JUNIOR', 'JUNIOR'), ('SENIOR', 'SENIOR')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('MARRIED', 'MARRIED'), ('SINGLE', 'SINGLE'), ('DIVORCED', 'DIVORCED'), ('DIVORCEE', 'DIVORCEE'), ('WIDOW', 'WIDOW'), ('WIDOWER', 'WIDOWER')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='nationality',
            field=models.CharField(blank=True, choices=[('NIGERIAN', 'NIGERIAN'), ('NON-CITIZEN', 'NON-CITIZEN')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='religion',
            field=models.CharField(blank=True, choices=[('ISLAM', 'ISLAM'), ('CHRISTIANITY', 'CHRISTIANITY'), ('TRADITIONAL', 'TRADITIONAL')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='zone',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='primary_qualification_type',
            field=models.CharField(blank=True, choices=[('TESTIMONIAL', 'TESTIMONIAL'), ('FIRST SCHOOL LEAVING CERTIFICATE', 'FIRST SCHOOL LEAVING CERTIFICATE')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='secondary_qualification_type',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('WAEC', 'WAEC')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='tertiary_institution_type',
            field=models.CharField(blank=True, choices=[('UNIVERSITY', 'UNIVERSITY'), ('POLYTECHNIC', 'POLYTECHNIC'), ('COLLEGE OF EDUCATION', 'COLLEGE OF EDUCATION')], max_length=300, null=True),
        ),
    ]
