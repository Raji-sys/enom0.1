# Generated by Django 4.1.7 on 2023-07-06 21:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import staff.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Retirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=300, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_school_name', models.CharField(blank=True, max_length=300, null=True)),
                ('primary_qualification_type', models.CharField(blank=True, max_length=300, null=True)),
                ('primary_qualification_date_obtained', models.DateField(blank=True, null=True)),
                ('secondary_school_name', models.CharField(blank=True, max_length=300, null=True)),
                ('secondary_qualification_type', models.CharField(blank=True, max_length=300, null=True)),
                ('secondary_qualification_date_obtained', models.DateField(blank=True, null=True)),
                ('tertiary_institution_type', models.CharField(blank=True, choices=[('university', 'University'), ('poly', 'Polytechnic'), ('college', 'College of education')], max_length=300, null=True)),
                ('tertiary_institution_name', models.CharField(blank=True, max_length=300, null=True)),
                ('tertiary_institution_qualification_type', models.CharField(blank=True, max_length=300, null=True)),
                ('tertiary_qualification_date_obtained', models.DateField(blank=True, null=True)),
                ('other_qualification_1', models.CharField(blank=True, max_length=300, null=True)),
                ('other_qualification_type_1', models.CharField(blank=True, max_length=300, null=True)),
                ('other_qualification_date_obtained_1', models.DateField(blank=True, null=True)),
                ('other_qualification_2', models.CharField(blank=True, max_length=300, null=True)),
                ('other_qualification_type_2', models.CharField(blank=True, max_length=300, null=True)),
                ('other_qualificiation_date_obtained_2', models.DateField(blank=True, null=True)),
                ('other_qualification_3', models.CharField(blank=True, max_length=300, null=True)),
                ('other_qualification_type_3', models.CharField(blank=True, max_length=300, null=True)),
                ('other_qualification_date_obtained_3', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_post', models.CharField(blank=True, max_length=300, null=True)),
                ('promotion_date', models.DateField(blank=True, null=True)),
                ('grade_level', models.IntegerField(blank=True, null=True)),
                ('step', models.IntegerField(blank=True, null=True)),
                ('incremented_date', models.DateField(blank=True, null=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professional_awarding_institute_name_1', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_awarding_institute_address_1', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_obtained_1', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_date_obtained_1', models.DateField(blank=True, null=True)),
                ('professional_awarding_institute_name_2', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_awarding_institute_address_2', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_obtained_2', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_date_obtained_2', models.DateField(blank=True, null=True)),
                ('professional_awarding_institute_name_3', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_awarding_institute_address_3', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_obtained_3', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_date_obtained_3', models.DateField(blank=True, null=True)),
                ('professional_awarding_institute_name_4', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_awarding_institute_address_4', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_obtained_4', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_date_obtained_4', models.DateField(blank=True, null=True)),
                ('professional_awarding_institute_name_5', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_awarding_institute_address_5', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_obtained_5', models.CharField(blank=True, max_length=300, null=True)),
                ('professional_qualification_date_obtained_5', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlename', models.CharField(blank=True, max_length=300, null=True)),
                ('staff_no', models.IntegerField(blank=True, null=True, unique=True, validators=[staff.models.valMax, django.core.validators.MaxValueValidator(999999)])),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widow', 'Widow'), ('Widower', 'Widower')], max_length=100, null=True)),
                ('place_of_birth', models.CharField(blank=True, max_length=150, null=True)),
                ('qualification', models.CharField(blank=True, max_length=150, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('Nigerian', 'Nigerian'), ('Non-Citizen', 'Non-Citizen')], max_length=200, null=True)),
                ('zone', models.CharField(blank=True, choices=[('North-East', 'North-East'), ('North-West', 'North-West'), ('North-Central', 'North-Central'), ('South-East', 'South-East'), ('South-West', 'South-West'), ('South-South', 'South-South')], max_length=300, null=True)),
                ('state', models.CharField(blank=True, choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa', 'Akwa'), ('Ibom', 'Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross-River', 'Cross-River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT-Abuja', 'Fct-Abuja'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nassarawa', 'Nassarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=30, null=True)),
                ('lga', models.CharField(blank=True, max_length=30, null=True)),
                ('senatorial_district', models.CharField(blank=True, max_length=50, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=300, null=True)),
                ('permanent_home_address', models.CharField(blank=True, max_length=300, null=True)),
                ('spouse', models.CharField(blank=True, max_length=300, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=300, null=True)),
                ('religion', models.CharField(blank=True, choices=[('Islam', 'Islam'), ('Christianity', 'Christianity'), ('Traditional', 'Traditional')], max_length=100, null=True)),
                ('number_of_children', models.IntegerField(blank=True, null=True)),
                ('name_of_children', models.TextField(blank=True, max_length=400, null=True)),
                ('dob_of_children', models.TextField(blank=True, max_length=300, null=True)),
                ('next_of_kin_1_fullname', models.CharField(blank=True, max_length=300, null=True)),
                ('next_of_kin_1_phone_number', models.IntegerField(blank=True, null=True)),
                ('next_of_kin_1_email', models.EmailField(blank=True, max_length=300, null=True)),
                ('next_of_kin_1_address', models.CharField(blank=True, max_length=300, null=True)),
                ('next_of_kin_1_relationship', models.CharField(blank=True, max_length=300, null=True)),
                ('next_of_kin_2_fullname', models.CharField(blank=True, max_length=300, null=True)),
                ('next_of_kin_2_phone_number', models.IntegerField(blank=True, null=True)),
                ('next_of_kin_2_email', models.EmailField(blank=True, max_length=300, null=True)),
                ('next_of_kin_2_address', models.CharField(blank=True, max_length=300, null=True)),
                ('next_of_kin_2_relationship', models.CharField(blank=True, max_length=300, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_of_leave', models.CharField(blank=True, max_length=300, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('total_days', models.IntegerField(blank=True, null=True)),
                ('remain', models.IntegerField(blank=True, null=True)),
                ('number_of_days_granted', models.IntegerField(null=True)),
                ('status', models.CharField(blank=True, max_length=300, null=True)),
                ('comment_if_any', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GovernmentAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('current_post', models.CharField(blank=True, max_length=30, null=True)),
                ('ippis_no', models.IntegerField(blank=True, null=True, unique=True, validators=[staff.models.vMax, django.core.validators.MaxValueValidator(999999)])),
                ('date_of_first_appointment', models.DateField(blank=True, null=True)),
                ('date_of_capt', models.DateField(blank=True, null=True)),
                ('type_of_appointment', models.CharField(blank=True, max_length=50, null=True)),
                ('salary_per_annum_at_date_of_first_appointment', models.FloatField(blank=True, max_length=300, null=True)),
                ('salary_scale', models.CharField(blank=True, max_length=300, null=True)),
                ('grade_level', models.CharField(blank=True, max_length=300, null=True)),
                ('step', models.IntegerField(blank=True, null=True)),
                ('type_of_cadre', models.CharField(blank=True, max_length=100, null=True)),
                ('exams_status', models.CharField(blank=True, max_length=100, null=True)),
                ('retire', models.CharField(blank=True, max_length=50, null=True)),
                ('rt_by', models.CharField(blank=True, max_length=50, null=True)),
                ('due', models.CharField(blank=True, max_length=100, null=True)),
                ('lv', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_post', models.CharField(blank=True, max_length=300, null=True)),
                ('date_of_appointment', models.DateField(blank=True, null=True)),
                ('status_current_out_of_office', models.CharField(blank=True, max_length=300, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offense', models.TextField(blank=True, null=True)),
                ('decision', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Disciplinaries',
            },
        ),
    ]
