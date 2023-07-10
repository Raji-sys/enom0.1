from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.db import models 


def valMax(v):
    mdigits=4
    vstr=str(v)
    if len(vstr)>mdigits:
        raise ValidationError(f'Maximum {mdigits} digits allowed')
    
class PersonalDetail(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


    middlename = models.CharField(max_length=300, null=True,blank=True)

    staff_no = models.IntegerField(null=True, unique=True, blank=True, validators=[valMax, MaxValueValidator(999999)])
    title = models.CharField(max_length=300, null=True, blank=True)
    sex=(('MALE','MALE'),('FEMALE','FEMALE'))
    gender = models.CharField(choices=sex, max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    m_status=(('MARRIED','MARRIED'), ('SINGLE','SINGLE'), ('DIVORCED','DIVORCED'), ('DIVORCEE','DIVORCEE'), ('WIDOW','WIDOW'), ('WIDOWER','WIDOWER'))
    marital_status = models.CharField(choices=m_status, max_length=100, null=True, blank=True)
    place_of_birth = models.CharField(max_length=150, null=True, blank=True)

    nationality_status=(('NIGERIAN','NIGERIAN'),('NON-CITIZEN','NON-CITIZEN'))   
    nationality = models.CharField(choices=nationality_status, max_length=200, null=True, blank=True)

    geo_political_zone=(('NORTH-EAST','NORTH-EAST'),('NORTH-WEST','NORTH-WEST'),('NORTH-CENTRAL','NORTH-CENTRAL'),('SOUTH-EAST','SOUTH-EAST'),('SOUTH-WEST','SOUTH-WEST'),('SOUTH-SOUTH','SOUTH-SOUTH'))
 
    # geo_political_zone=models.TextChoices('GEO_POLITICAL_ZONE','NORTH-EAST NORTH-WEST NORTH-CENTRAL SOUTH-EAST SOUTH-WEST SOUTH-SOUTH')
    zone = models.CharField(blank=True, choices=geo_political_zone, max_length=300, null=True)


    state=models.CharField(blank=True,max_length=300, null=True)
    lga=models.CharField(blank=True,max_length=300, null=True)
    senatorial_district = models.CharField(max_length=300, null=True, blank=True)
    
    residential_address = models.CharField(max_length=300, null=True, blank=True)
    permanent_home_address = models.CharField(max_length=300, null=True, blank=True)
    
    spouse = models.CharField(max_length=300, null=True, blank=True)
    hobbies = models.CharField(max_length=300, null=True, blank=True)
    faith=(('ISLAM', 'ISLAM'), ('CHRISTIANITY','CHRISTIANITY'),('TRADITIONAL', 'TRADITIONAL'))
    religion = models.CharField(choices=faith, max_length=100, null=True, blank=True)

    qualification=models.CharField(max_length=150, null=True,blank=True)
    
    number_of_children = models.IntegerField(null=True, blank=True)
    name_of_children = models.TextField(max_length=400, null=True, blank=True)
    dob_of_children = models.TextField(max_length=300, null=True, blank=True)
    # passport = models.ImageField(null=True)

    next_of_kin_1_fullname = models.CharField(max_length=300, null=True, blank=True)
    next_of_kin_1_phone_number = models.IntegerField(null=True, blank=True)
    next_of_kin_1_email = models.EmailField(max_length=300, null=True, blank=True)
    next_of_kin_1_address = models.CharField(max_length=300, null=True, blank=True)
    next_of_kin_1_relationship = models.CharField(max_length=300, null=True, blank=True)
    # next_of_kin_1_passport = models.ImageField(null=True)

    next_of_kin_2_fullname = models.CharField(max_length=300, null=True, blank=True)
    next_of_kin_2_phone_number = models.IntegerField(null=True, blank=True)
    next_of_kin_2_email = models.EmailField(max_length=300, null=True, blank=True)
    next_of_kin_2_address = models.CharField(max_length=300, null=True, blank=True)
    next_of_kin_2_relationship = models.CharField(max_length=300, null=True, blank=True)
    # next_of_kin_2_passport = models.ImageField(null=True)
    
    timestamp = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return "{} {}: {}".format(self.user.first_name, self.user.last_name, self.staff_no)
    
    
    def age(self):
        today=date.today()
        if self.date_of_birth:
            age=today.year-self.date_of_birth.year

            if today.month<self.date_of_birth.month or (today.month==self.date_of_birth.month and today.day < self.date_of_birth.day):
                age-=1        
            return age 
    
    def dob(self):
        today=date.today()
        if self.date_of_birth is not None:
            is_dob=today.month==self.date_of_birth.month and today.day ==self.date_of_birth.day
            if is_dob:
                return is_dob


class Qualification(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    primary_school_name = models.CharField(max_length=300,null=True, blank=True)

    pc=(('TESTIMONIAL','TESTIMONIAL'), ('FIRST SCHOOL LEAVING CERTIFICATE','FIRST SCHOOL LEAVING CERTIFICATE'))
    primary_qualification_type = models.CharField(choices=pc, max_length=300,null=True,blank=True)
    
    primary_qualification_date_obtained = models.DateField(null=True,blank=True)

    secondary_school_name = models.CharField(max_length=300,null=True,blank=True)
    sc=(('WAEC','WAEC'), ('NECO','NECO'),('WAEC','WAEC'))
    secondary_qualification_type = models.CharField(choices=sc, max_length=300,null=True,blank=True)
    secondary_qualification_date_obtained = models.DateField(null=True,blank=True)

    type_of_tertiary=(('UNIVERSITY', 'UNIVERSITY'), ('POLYTECHNIC','POLYTECHNIC'), ('COLLEGE OF EDUCATION','COLLEGE OF EDUCATION'))
    tertiary_institution_type = models.CharField(choices=type_of_tertiary, max_length=300,null=True,blank=True)
    tertiary_institution_name = models.CharField(max_length=300,null=True,blank=True)
    tertiary_institution_qualification_type = models.CharField(max_length=300,null=True,blank=True)
    tertiary_qualification_date_obtained = models.DateField(null=True,blank=True)

    other_qualification_1 = models.CharField(max_length=300,null=True,blank=True)
    other_qualification_type_1 = models.CharField(max_length=300,null=True,blank=True)
    other_qualification_date_obtained_1 = models.DateField(null=True,blank=True)

    other_qualification_2 = models.CharField(max_length=300,null=True,blank=True)
    other_qualification_type_2 = models.CharField(max_length=300,null=True,blank=True)
    other_qualificiation_date_obtained_2 = models.DateField(null=True,blank=True)

    other_qualification_3 = models.CharField(max_length=300,null=True,blank=True)
    other_qualification_type_3 = models.CharField(max_length=300,null=True,blank=True)
    other_qualification_date_obtained_3 = models.DateField(null=True,blank=True)

    timestamp = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class ProfessionalQualification(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    professional_awarding_institute_name_1 = models.CharField(max_length=300,null=True,blank=True)
    professional_awarding_institute_address_1 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_obtained_1 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_date_obtained_1 = models.DateField(null=True,blank=True)

    professional_awarding_institute_name_2 = models.CharField(max_length=300,null=True,blank=True)
    professional_awarding_institute_address_2 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_obtained_2 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_date_obtained_2 = models.DateField(null=True,blank=True)

    professional_awarding_institute_name_3 = models.CharField(max_length=300,null=True,blank=True)
    professional_awarding_institute_address_3 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_obtained_3 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_date_obtained_3 = models.DateField(null=True,blank=True)

    professional_awarding_institute_name_4 = models.CharField(max_length=300,null=True,blank=True)
    professional_awarding_institute_address_4 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_obtained_4 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_date_obtained_4 = models.DateField(null=True,blank=True)

    professional_awarding_institute_name_5 = models.CharField(max_length=300,null=True,blank=True)
    professional_awarding_institute_address_5 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_obtained_5 = models.CharField(null=True,max_length=300,blank=True)
    professional_qualification_date_obtained_5 = models.DateField(null=True,blank=True)

    timestamp = models.DateTimeField('date added',auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)



def vMax(v):
    mdigits=6
    vstr=str(v)
    if len(vstr)>mdigits:
        raise ValidationError(f'Maximum {mdigits} digits allowed')


class GovernmentAppointment(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    dep=(
         ('ADMINISTRATION','ADMINISTRATION'),
         ('ACCOUNT','ACCOUNT'),
         ('BIO-MEDICAL ENGINEERING','BIO-MEDICAL ENGINEERING'),
         ('CLINICAL SERVICES','CLINICAL SERVICES'),
         ('CATERING','CATERING'),
         ('DISCIPLINE','DISCIPLINE'),
         ('ENGINEERING','ENGINEERING'),
         ('INFORMATION TECHNOLOGY','INFORMATION TECHNOLOGY'),
         ('INTERNAL AUDIT','INTERNAL AUDIT'),
         ('LEGAL','LEGAL'),
         ('LIBRARY','LIBRARY'),
         ('MEDICAL RECORD','MEDICAL RECORD'),
         ('MEDICAL ILLUSTRATION','MEDICAL ILLUSTRATION'),
         ('NURSING EDUCATION','NURSING EDUCATION'),
         ('NURSING SERVICES','NURSING SERVICES'),
         ('PATHOLOGY','PATHOLOGY'),
         ('PHARMACY','PHARMACY'),
         ('PHYSIOTHERAPHY','PHYSIOTHERAPHY'),
         ('PROSTHETIC AND ORTHOTICS','PROSTHETIC AND ORTHOTICS'),
         ('PROCUMENT','PROCUMENT'),
         ('PUBLIC HEALTH','PUBLIC HEALTH'),
         ('OCCUPATIONAL THERAPHY','OCCUPATIONAL THERAPHY'),
         ('RADIOLOGY','RADIOLOGY'),
         ('SERVICOM','SERVICOM'),
         ('SOCIAL WELFARE','SOCIAL WELFARE'),
         ('STORE','STORE'),
         ('TELEPHONE','TELEPHONE'),
         ('TRANSPORT','TRANSPORT'),
         )
    department=models.CharField(choices=dep, blank=True,max_length=300, null=True)
    current_post=models.CharField(blank=True,max_length=300, null=True)
   
    ippis_no = models.IntegerField(null=True, unique=True, blank=True,validators=[vMax,MaxValueValidator(999999)])

    date_of_first_appointment = models.DateField(null=True,blank=True)
    date_of_capt = models.DateField(null=True,blank=True)

    tp=(('CASUAL','CASUAL'),('LOCUM','LOCUM'),('PERMANENT','PERMANENT'),('PROBATION', 'PROBATION'))
    type_of_appointment=models.CharField(choices=tp, null=True,max_length=300,blank=True)
    
    salary_per_annum_at_date_of_first_appointment = models.FloatField(null=True,max_length=300,blank=True)
    
    ss=(('CONHESS','CONHESS'),('CONMESS','CONMESS'), ('GIPMIS','GIPMIS'))
    salary_scale = models.CharField(choices=ss, null=True,max_length=300,blank=True)
    
    gl=(('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),('09','09'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'))
    grade_level = models.CharField(choices=gl, null=True,max_length=300,blank=True)
    step = models.IntegerField(null=True, blank=True)

    tc=(('JUNIOR','JUNIOR'), ('SENIOR','SENIOR'))
    type_of_cadre=models.CharField(choices=tc, null=True, blank=True, max_length=100)

    exams_status = models.CharField(null=True, blank=True, max_length=100)
    retire=models.CharField(null=True, blank=True,max_length=50)
    rt_by=models.CharField(null=True, blank=True,max_length=50)
    due=models.CharField(null=True, blank=True,max_length=100)
    lv=models.CharField(null=True,blank=True,max_length=100)
    timestamp = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.first_name} {self.user.last_name}"

 
class Promotion(models.Model):
    emp = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    current_post = models.CharField(null=True,max_length=300,blank=True)
    promotion_date = models.DateField(null=True,blank=True)
    grade_level = models.IntegerField(null=True,blank=True)
    step = models.IntegerField(null=True,blank=True)
    incremented_date = models.DateField(null=True,blank=True)
    confirmation_date = models.DateField(null=True,blank=True)
    timestamp = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        if self.emp:
            return f"{self.emp.last_name} {self.emp.first_name}"


class Discipline(models.Model):
    emp = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    offense = models.TextField(null=True,blank=True)
    decision = models.TextField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField('date added', auto_now_add=True)

    class Meta:
        verbose_name_plural='Disciplinaries'

    def __str__(self):
        if self.emp:
            return f"{self.emp.last_name} {self.emp.first_name}"


class Leave(models.Model):
    emp = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nature_of_leave = models.CharField(null=True,max_length=300,blank=True)
    year = models.IntegerField(null=True,blank=True)
    start_date = models.DateField(null=True,blank=False)
    return_date = models.DateField(null=True,blank=True)
    total_days=models.IntegerField(null=True, blank=True)
    remain=models.IntegerField(null=True,blank=True)

    number_of_days_granted = models.IntegerField(null=True, blank=False)
    status = models.CharField(null=True,max_length=300,blank=True)
    comment_if_any = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField('date added', auto_now_add=True)
       
    def __str__(self):
        if self.emp:
            return f"{self.emp.last_name} {self.emp.first_name}"

                      
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    def remaining_days(self):
        if self.total_days is not None and self.number_of_days_granted is not None:
            return self.total_days - self.number_of_days_granted
        return 0

    def clean(self):
        super().clean()

        r = self.remaining_days()
        if r < 0 or self.number_of_days_granted == 0:
            raise ValidationError('Invalid entry. Please try again.')
        
                
        # self.remain = r
        # if self.total_days is not None and self.remain is not None and self.remain != r:
        #     raise ValidationError('Invalid entry. Remaining days do not match total days.')
         
    def u_return_date(self):
        if self.number_of_days_granted is not None:
            if self.number_of_days_granted > 0:
                ddays=self.total_days-self.remaining_days()
                timedelta_o=timedelta(days=ddays)
                new_date=self.start_date+timedelta_o
                if new_date is not None:
                    return new_date
    

class ExecutiveAppointment(models.Model):
    emp = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    designation_post = models.CharField(null=True,max_length=300,blank=True)
    date_of_appointment = models.DateField(null=True,blank=True)
    status_current_out_of_office = models.CharField(null=True,max_length=300,blank=True)
    timestamp = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        if self.emp:
            return f"{self.emp.last_name} {self.emp.first_name}"


class Retirement(models.Model):
    emp = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_retired = models.DateField(null=True,blank=True)
    status = models.CharField(null=True,max_length=300,blank=True)
    timestamp = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        if self.emp:
            return f"{self.emp.last_name} {self.emp.first_name}"