from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *
from ems.forms import *
from ems.decorators import unauthenticated_user, allowed_users
from django.contrib import messages
from .filters import *
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from django.forms import inlineformset_factory
from io import BytesIO
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.utils.dateformat import DateFormat 
from datetime import  date
from django.shortcuts import render
from utils.ufun import con
from django.http import JsonResponse



#this functions generates csv reports with headers and body
#using the python built-in csv package
@login_required(login_url='ems:login')
@allowed_users(allowed_roles=['admin'])
#@admin_only
def csvFile(request):    
    response=HttpResponse(content_type='text/csv',headers={'Content-Disposition':'attachment; filename="report_.csv"'},)    

    writer=csv.writer(response)
    user=User.objects.all()
   
    govFilter=GovFilter(request.GET, queryset=user)

    user=govFilter.qs
    # result=request.GET['date_of_first_appointment']

    #csv headers            
    # writer.writerow(['','','','','','','Data of {} staff'.format(result) ])
    writer.writerow([])
    writer.writerow([])
    writer.writerow([
                    'NAME','FILE NO','IPPIS','DATE OF BIRTH','STATE','LGA','QUALIFICATION',
                    'DATE OF 1ST APPOINTMENT','DATE OF CURRENT APPOINTMENT','CURRENT POST',
                    'DEPARTMENT','GRADE LEVEL','ZONE'])


    #generate csv body data with variables using foor loop 
    for u in user:
        #using this function in combing the grade level and step datas in on field
        #using and underscore(_) to show their sepration
        #also preventing empty fields from returning None
        def co():
            d = str('_')
            if u.governmentappointment.grade_level is None:
                d=''
            if u.governmentappointment.step is None:
                d=''
            return d

        #mixing the grade level field with the step field
        c=str(con(u.governmentappointment.grade_level))+str(co())+str(con(u.governmentappointment.step))

        #filling the body with field data
        #converting each result to string with py str() method
        #call the utility function con to stop empty fields from returning None 
        writer.writerow([
            str(u.first_name).upper()+str(' ')+str(con(u.personaldetail.middlename)).upper()+str(' ')+str(u.last_name).upper(),
            u.personaldetail.staff_no, 
            u.governmentappointment.ippis_no,
            u.personaldetail.date_of_birth,
            str(con(u.personaldetail.state).upper()),
            str(con(u.personaldetail.lga).upper()),
            str(con(u.personaldetail.qualification).upper()),
            u.governmentappointment.date_of_first_appointment,
            u.governmentappointment.date_of_capt,
            str(con(u.governmentappointment.current_post).upper()),
            str(con(u.governmentappointment.department).upper()),
            c,
            str(con(u.personaldetail.zone).upper()),])
    
    return response


#this functions generates pdf reports with headers and body
#using reportlap package
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='ems:login')
#@admin_only
def pdfFile(request):

    user=User.objects.all()

    govFilter=GovFilter(request.GET, queryset=user)
    user=govFilter.qs

    # Prepend the header row
    data = [[
            'NAME','FILE NO','IPPIS','DATE OF BIRTH','STATE','LGA','QUALIFICATION',
            'DATE OF FIRST APPT','DATE OF CURRENT APPT','CURRENT POST',
            'DEPARTMENT','GRADE LEVEL','ZONE']]
    

    #generate pdf body data with variables using foor loop 
    for u in user:

        #checking if data is available before proceeding to convert the date format
        #for date of first appointment
        if u.governmentappointment.date_of_first_appointment is not None:
            date_of_1st_appt=DateFormat(u.governmentappointment.date_of_first_appointment).format('d-m-Y')
        else:
            date_of_1st_appt=''

        #checking if data is available before proceeding to convert the date format
        #for date of birth
        if u.personaldetail.date_of_birth is not None:
            dob=DateFormat(u.personaldetail.date_of_birth).format('d-m-Y')
        else:
            dob=''

        #checking if data is available before proceeding to convert the date format
        #for date of current appointment
        if u.governmentappointment.date_of_capt is not None:
            date_of_capt=DateFormat(u.governmentappointment.date_of_capt).format('d-m-Y')
        else:
            date_of_capt=''

        #populating pdf table with row data
        #converting each result to string with py str() method
        #call the utility function con to stop empty fields from returning None 
        row = [
            str(u.first_name).upper()+str(' ')+str(con(u.personaldetail.middlename)).upper()+str(' ')+str(u.last_name).upper(),
            u.personaldetail.staff_no,
            u.governmentappointment.ippis_no,
           #calling the date processing functionality
            dob,
            str(con(u.personaldetail.state).upper()),
            str(con(u.personaldetail.lga).upper()),
            str(con(u.personaldetail.qualification).upper()),
           #calling the date processing functionality
            date_of_1st_appt,
           #calling the date processing functionality
            date_of_capt,
            str(con(u.governmentappointment.current_post).upper()),
            str(con(u.governmentappointment.department).upper()),
            str(con(u.governmentappointment.grade_level))+str('/')+str(con(u.governmentappointment.step)),
            str(con(u.personaldetail.zone).upper()),
            ]
        
        data.append(row)

    #preparing the content type and a default pdf file name 'report'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    # Create a buffer object to hold the PDF
    buffer = BytesIO()

    #pdf table location and page orientation
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4),topMargin=30)
    table=Table(data)

    # Defining the table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('SIZE', (0, 0), (-1, -1), 7.5),
        ('LEADING', (0, 0), (-1, -1), 8.2),
    ])
    table.setStyle(table_style)
    table.rotate=90

    # Add the table to the document and build the PDF
    elements = []
    elements.append(table)
    doc.build(elements)

    # Get the value of the buffer and write it to the response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

 
 #view function for displaying all employees
#@admin_only
@login_required(login_url='ems:login')
@allowed_users(allowed_roles=['admin'])
def staffView(request):
    
    User=get_user_model()
    users=User.objects.all()

    total=users.filter(is_active=True, is_superuser=False).count()

    #search using by file number filter
    staffFilter=StaffFilter(request.GET, queryset=users)
    
    #ordering method 
    users=staffFilter.qs.order_by('-date_joined')
    # users=staffFilter.qs.order_by('personaldetail__staff_no')
  

    #pagination functionality
    paginator = Paginator(users,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    result=request.GET.get('date_of_first_appointment')

    context = { 
        'staffFilter':staffFilter, 
                 'users':users,
                  'page_obj':page_obj,
                  'result':result,
                  'total':total,
                   }
    return render(request, 'staff/stafflist.html', context)


#stats display view function
#@admin_only
@login_required(login_url='ems:login')
@allowed_users(allowed_roles=['admin'])
def stats(request,):
    
    User=get_user_model()
    users=User.objects.all()
    total=users.filter(is_active=True, is_superuser=False).count()
  
    #gender count
    male=PersonalDetail.objects.filter(gender__iexact='Male').count()
    female=PersonalDetail.objects.filter(gender__iexact='Female').count()

    #geo zone count
    ne=PersonalDetail.objects.filter(zone__iexact='north-east').count()
    nw=PersonalDetail.objects.filter(zone__iexact='north-west').count()
    nc=PersonalDetail.objects.filter(zone__iexact='north-central').count()
    se=PersonalDetail.objects.filter(zone__iexact='south-east').count()
    sw=PersonalDetail.objects.filter(zone__iexact='south-west').count()
    ss=PersonalDetail.objects.filter(zone__iexact='south-south').count()

    #state count
    abia=PersonalDetail.objects.filter(state__iexact='abia').count()
    adamawa=PersonalDetail.objects.filter(state__iexact='adamawa').count()
    akwa_ibom=PersonalDetail.objects.filter(state__iexact='akwa ibom').count()
    anambra=PersonalDetail.objects.filter(state__iexact='anambra').count()
    bauchi=PersonalDetail.objects.filter(state__iexact='bauchi').count()
    bayelsa=PersonalDetail.objects.filter(state__iexact='bayelsa').count()
    benue=PersonalDetail.objects.filter(state__iexact='benue').count()
    borno=PersonalDetail.objects.filter(state__iexact='borno').count()
    cross_river=PersonalDetail.objects.filter(state__iexact='cross_river').count()
    delta=PersonalDetail.objects.filter(state__iexact='delta').count()
    ebonyi=PersonalDetail.objects.filter(state__iexact='ebonyi').count()
    edo=PersonalDetail.objects.filter(state__iexact='edo').count()
    ekiti=PersonalDetail.objects.filter(state__iexact='ekiti').count()
    enugu=PersonalDetail.objects.filter(state__iexact='enugu').count()
    fct_abuja=PersonalDetail.objects.filter(state__iexact='fct-abuja').count()
    gombe=PersonalDetail.objects.filter(state__iexact='gombe').count()
    imo=PersonalDetail.objects.filter(state__iexact='imo').count()
    jigawa=PersonalDetail.objects.filter(state__iexact='jigawa').count()
    kaduna=PersonalDetail.objects.filter(state__iexact='kaduna').count()
    kano=PersonalDetail.objects.filter(state__iexact='kano').count()
    katsina=PersonalDetail.objects.filter(state__iexact='katsina').count()
    kebbi=PersonalDetail.objects.filter(state__iexact='kebbi').count()
    kogi=PersonalDetail.objects.filter(state__iexact='kogi').count()
    kwara=PersonalDetail.objects.filter(state__iexact='kwara').count()
    nassarawa=PersonalDetail.objects.filter(state__iexact='nassarawa').count()
    niger=PersonalDetail.objects.filter(state__iexact='niger').count()
    ogun=PersonalDetail.objects.filter(state__iexact='ogun').count()
    osun=PersonalDetail.objects.filter(state__iexact='osun').count()
    ondo=PersonalDetail.objects.filter(state__iexact='ondo').count()
    oyo=PersonalDetail.objects.filter(state__iexact='oyo').count()
    plateau=PersonalDetail.objects.filter(state__iexact='plateau').count()
    rivers=PersonalDetail.objects.filter(state__iexact='rivers').count()
    sokoto=PersonalDetail.objects.filter(state__iexact='sokoto').count()
    taraba=PersonalDetail.objects.filter(state__iexact='taraba').count()  
    yobe=PersonalDetail.objects.filter(state__iexact='yobe').count()
    zamfara=PersonalDetail.objects.filter(state__iexact='zamfara').count()

    #lga count
    dala=PersonalDetail.objects.filter(lga__iexact='dala').count()
    kano_municipal=PersonalDetail.objects.filter(state__iexact='kano_municipal').count()

    #marital status count
    married=PersonalDetail.objects.filter(marital_status__iexact='married').count()
    single=PersonalDetail.objects.filter(marital_status__iexact='single').count()
    divorced=PersonalDetail.objects.filter(marital_status__iexact='divorced').count()
    widow=PersonalDetail.objects.filter(marital_status__iexact='widow').count()
    widower=PersonalDetail.objects.filter(marital_status__iexact='widower').count()

    #religion count
    islam=PersonalDetail.objects.filter(religion__iexact='islam').count()
    christianity=PersonalDetail.objects.filter(religion__iexact='christianity').count()
    traditional=PersonalDetail.objects.filter(religion__iexact='traditional').count()

    #grade level count
    gl_03=GovernmentAppointment.objects.filter(grade_level__iexact='3').count()
    gl_04=GovernmentAppointment.objects.filter(grade_level__iexact='4').count()
    gl_05=GovernmentAppointment.objects.filter(grade_level__iexact='5').count()
    gl_06=GovernmentAppointment.objects.filter(grade_level__iexact='6').count()
    gl_07=GovernmentAppointment.objects.filter(grade_level__iexact='7').count()
    gl_08=GovernmentAppointment.objects.filter(grade_level__iexact='8').count()
    gl_09=GovernmentAppointment.objects.filter(grade_level__iexact='9').count()
    gl_11=GovernmentAppointment.objects.filter(grade_level__iexact='11').count()
    gl_12=GovernmentAppointment.objects.filter(grade_level__iexact='12').count()
    gl_13=GovernmentAppointment.objects.filter(grade_level__iexact='13').count()
    gl_14=GovernmentAppointment.objects.filter(grade_level__iexact='14').count()
    gl_15=GovernmentAppointment.objects.filter(grade_level__iexact='15').count()
 
    #cadre/current post count
    asst_director=GovernmentAppointment.objects.filter(current_post__iexact='asst_director').count()

    chief_acct=GovernmentAppointment.objects.filter(current_post__iexact='chief_accountant').count()
    asst_chief_acct=GovernmentAppointment.objects.filter(current_post__iexact='asst_chief_accountant').count()
    prin_acct=GovernmentAppointment.objects.filter(current_post__iexact='prinicipal_accountant').count()
    chief_exec_off_acct=GovernmentAppointment.objects.filter(current_post__iexact='chief exec. off. accountant').count()
    acct_I=GovernmentAppointment.objects.filter(current_post__iexact='accountant I').count()
    acct_II=GovernmentAppointment.objects.filter(current_post__iexact='accountant II').count()
    senior_exec_off_acct=GovernmentAppointment.objects.filter(current_post__iexact='senior exec. off. acccount').count()
    prin_exec_off_acct_I=GovernmentAppointment.objects.filter(current_post__iexact='principal exec. off. accountant I').count()
    prin_exec_off_acct_II=GovernmentAppointment.objects.filter(current_post__iexact='principal exec. off. accountant II').count()
    higher_exec_off_acct=GovernmentAppointment.objects.filter(current_post__iexact='higher executive officer acct').count()
    exec_off_acct=GovernmentAppointment.objects.filter(current_post__iexact='executive officer acct').count()



    consultant=GovernmentAppointment.objects.filter(current_post__iexact='consultant').count()

    #salary scale count
    conhess=GovernmentAppointment.objects.filter(salary_scale__iexact='conhess').count()
    conmess=GovernmentAppointment.objects.filter(salary_scale__iexact='conmess').count()

    #department count
    account=GovernmentAppointment.objects.filter(department__iexact='account').count()
    record=GovernmentAppointment.objects.filter(department__iexact='record').count()
    clinical_service=GovernmentAppointment.objects.filter(department__iexact='clinical services').count()

   
    # depFilter=DepFilter(request.GET, queryset=users)

  
    context = { 
                'total':total, 'male':male,'female':female,
                
                'ne':ne, 'nw':nw, 'nc':nc, 'se':se, 'sw':sw, 'ss':ss,

                'abia':abia,'adamawa':adamawa,'akwa_ibom':akwa_ibom,'anambra':anambra,
                'bauchi':bauchi,'bayelsa':bayelsa,'benue':benue,'borno':borno,
                'cross_river':cross_river,'delta':delta,'ebonyi':ebonyi,'edo':edo,
                'ekiti':ekiti,'enugu':enugu,'fct_abuja':fct_abuja,'gombe':gombe,'imo':imo,
                'jigawa':jigawa,'kaduna':kaduna,'kano':kano,'katsina':katsina,
                'kebbi':kebbi,'kogi':kogi,'kwara':kwara,'nassarawa':nassarawa,
                'niger':niger,'ogun':ogun,'osun':osun,'ondo':ondo,'oyo':oyo,
                'plateau':plateau,'rivers':rivers,'sokoto':sokoto,'taraba':taraba,
                'yobe':yobe,'zamfara':zamfara,

                'dala':dala, 'kano_municipal':kano_municipal,

                'married':married,'single':single,'divorced':divorced,'widow':widow,'widower':widower,

                'islam':islam,'christianity':christianity,'traditional':traditional,

                'gl_07':gl_07,'gl_08':gl_08,

                'conhess':conhess,'conmess':conmess,

                'consultant':consultant,
                
                'account':account,'record':record,'clinical_service':clinical_service,
               }
    
    return render(request, 'staff/stats.html', context)


#notice display view function
#@admin_only
@login_required(login_url='ems:login')
@allowed_users(allowed_roles=['admin'])
def notice(request,):
    
    User=get_user_model()
    users=User.objects.all()

     #DUE FOR PROMOTION count
    due=GovernmentAppointment.objects.filter(due__iexact='ok').count()
    #list of all those DUE FOR PROMOTION
    dueA=GovernmentAppointment.objects.filter(due='ok').all()
    dueA=GovernmentAppointment.objects.filter(due='ok')

     #DUE FOR RETIREMENT count
    rt=GovernmentAppointment.objects.filter(retire__iexact='rt').count()
    #list of all those DUE FOR PROMOTION
    rtA=GovernmentAppointment.objects.filter(retire='rt').all()
    
    lv=GovernmentAppointment.objects.filter(lv__iexact='over').count()
    lvA=GovernmentAppointment.objects.filter(lv='over').all()
    lve=GovernmentAppointment.objects.filter(lv='over')

    prom = []
    for d in dueA:
        pr = PersonalDetail.objects.get(user=d.user)
        prom.append(pr)    
    
    ret = []
    for r in rtA:
        rti = PersonalDetail.objects.get(user=r.user)
        ret.append(rti)    

    personal_details = []
    for l in lve:
        # Get the PersonalDetail object associated with each GovernmentAppointment
        # personal_detail = l.user.personaldetail
        personal_detail = PersonalDetail.objects.get(user=l.user)
        personal_details.append(personal_detail)    
    # if lve:
    #     # Get the PersonalDetail object associated with the GovernmentAppointment
    #     personal_detail = lve.user.personaldetail

    context={'due':due, 'dueA':dueA, 'rt':rt,'rtA':rtA,'lv':lv,'lvA':lvA,
             'personal_details':personal_details,'prom':prom,'ret':ret}

    return render(request, 'staff/notice.html', context)



#report generation page for both excel and pdf
#@admin_only
@login_required(login_url='ems:login')
@allowed_users(allowed_roles=['admin'])
def report(request):
    
    User=get_user_model()
    users=User.objects.all()
   
    total=users.filter(is_active=True, is_superuser=False).count()

    # adding users to government appointment filter  
    govFilter=GovFilter(request.GET, queryset=users)

    # users=govFilter.qs.order_by('last_name')
    # users=govFilter.qs.order_by('personaldetail__staff_no')
    users=govFilter.qs.order_by('governmentappointment__department')
    
    #pagination functionality
    paginator = Paginator(users, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    result = request.GET.get('date_of_first_appointment')

    # dep=request.GET.get('department')

    context = {'govFilter':govFilter,'users':users,'page_obj':page_obj,'result':result,'total':total}

    return render(request, 'staff/report.html', context)


#staff details page for displaying all informtion in staff file
@login_required(login_url='ems:login')
@allowed_users(allowed_roles=['admin'])
def staffDetail(request, pk):

    User=get_user_model()
    users=User.objects.get(id=pk)

    #querying employee data from various models as the name suggests
    emp=users.promotion_set.all()
    dis=users.discipline_set.all()
    liv=users.leave_set.all()
    execapp=users.executiveappointment_set.all()
    retire=users.retirement_set.all()

    #calculating step increment annually
    #creating the neccessary variables    
    today=date.today()
    d=today.year
    
    #function to increment employee step automatically annually
    def step_inc():
        #if government appointment model step field is available and the date is 
        #1st january,  
        if users.governmentappointment.step and today == date(d,1,1):
            #increment the step 
            users.governmentappointment.step += 1
            #call the save function
            users.governmentappointment.save()

    #calling the function
    step_inc()
        

    #promotion determinate function
    def promotion():
        # performing checks
        if users.governmentappointment.date_of_capt is not None:
            #naming variables
            cal=users.governmentappointment.date_of_capt.year
            ex=users.governmentappointment.exams_status
            gl=users.governmentappointment.grade_level
            tc=users.governmentappointment.type_of_cadre
            
            #performing checks
            if cal is not None:
                #if the current year minus (-) date of current appoitnment is equals 3
                #and grade level is greater than or equal 6
                #and exams status is equals pass 
                #and type of cadre is senior
                if today.year-cal  == 3 and int(gl) >= 6 and ex == 'pass' and tc == 'senior':
                    #then staff is DUE FOR PROMOTION and the 'ok' string flag is added to 
                    # government appointment model due field 
                    users.governmentappointment.due = 'ok'  
                    #saving the changes  
                    users.governmentappointment.save()
                    #return the message string 'DUE FOR PROMOTION'
                    return messages.success(request,'DUE FOR PROMOTION')
                elif today.year-cal  == 2 and int(gl) <= 5 and ex == 'pass' and tc == 'junior':
                    #or if the current year minus (-) date of current appoitnment is equals 2
                    #and grade level is greater than or equal 5
                    #and exams status is equals pass 
                    #and type of cadre is junior
                    users.governmentappointment.due = 'ok'    
                    # ok' string flag is added to 
                    # government appointment model due field 
                    users.governmentappointment.save()
                    #save changes
                    return messages.success(request,'DUE FOR PROMOTION')
                    # return successs message
                elif today.year-cal  == 4 and int(gl) >= 13 and ex == 'pass' and tc == 'executive':
                    #or if the current year minus (-) date of current appoitnment is equals 4
                    #and grade level is greater than or equal 13
                    #and exams status is equals pass 
                    #and type of cadre is executive
                    users.governmentappointment.due = 'ok'    
                    # ok' string flag is added to 
                    # government appointment model due field 
                    users.governmentappointment.save()
                    #save changes
                    return messages.success(request,'DUE FOR PROMOTION')
                    #return success meesage
                else:
                    users.governmentappointment.due = ' '
                    #else level the government appointment model due field empty
                    users.governmentappointment.save()
                    #save changes
                    return messages.success(request,' ')       
                    #success message blank

    #calling the function live
    promotion() 

    #retirement determinate function
    def rt():
        #name varaibles
        art=users.personaldetail.age()
        drt=users.governmentappointment.date_of_first_appointment
        #performing checks
        if drt is not None:
            #if date of first appoitnment is available drt is
            #current year minus (-) the year of first appointment
            drt=today.year-drt.year
        #if staff age is available and is greater than or equal 65
        if art is not None and art >= 65:
            #government app model retire field is the string 'rt'
            users.governmentappointment.retire = "rt"
            #government app model rt_by field is the string 'rtd by dob'
            users.governmentappointment.rt_by = "RETIRE BY DOB"
            #save changes
            users.governmentappointment.save()
            #or if date of first appointment is available and year of 
            # 1st appointment is greater than or equal to 35
        elif drt is not None and drt >= 35:
            #government app model retire field is the string 'rt'
            users.governmentappointment.retire = "rt"
            #government app model rt_by field is the string 'rtd by dofa'
            users.governmentappointment.rt_by = "RETIRE BY DOFA"
            #save changes
            users.governmentappointment.save()
        else:
            users.governmentappointment.retire = " "
            users.governmentappointment.save()

    # calling the function live
    rt()


    def lv():
        leaves = Leave.objects.all()
        for lv in leaves:
            remaining_days = lv.remaining_days()
            government_appointment = users.governmentappointment  # Replace this with the appropriate way to retrieve the government appointment object
        
            if remaining_days is not None and remaining_days <= 0:
                government_appointment.lv = 'over'
            else:
                government_appointment.lv = ''
            government_appointment.save()
    lv()

    context = {'users':users,'emp':emp,
               'dis':dis,'liv':liv,
               'execapp':execapp,'retire':retire,
               'd':d,'rt':rt,'promotion':promotion,
               'step_inc':step_inc}
    
    return render(request, 'staff/staffdetail.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateForm(request, pk):

    user=User.objects.get(id=pk)
    userform = userForm(instance=user)
    profileform = PersonalDetailForm(instance=user.personaldetail)
    qualform = QualForm(instance=user.qualification)
    proqualform = ProQualForm(instance=user.professionalqualification)
    govtappform = GovtAppForm(instance=user.governmentappointment)

    if request.method == 'POST':
        userform = userForm(request.POST, instance=user)
        profileform = PersonalDetailForm(request.POST, instance=user.personaldetail)
        qualform = QualForm(request.POST, instance=user.qualification)
        proqualform = ProQualForm(request.POST, instance=user.professionalqualification)
        govtappform = GovtAppForm(request.POST, instance=user.governmentappointment)

        if userform.is_valid() and profileform.is_valid() and qualform.is_valid() and proqualform.is_valid() and govtappform.is_valid():
        # if profileform.is_valid() and qualform.is_valid() and proqualform.is_valid() and govtappform.is_valid():
            userform.save()
            profileform.save()
            qualform.save()
            proqualform.save()
            govtappform.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated, {} {}'.format(
                request.user, user.last_name,user.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[user.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
            # messages.error(request, ('please go back and correct the error'))


    context = {'userform':userform,'profileform': profileform, 
               'qualform': qualform,'proqualform':proqualform,
               'govtappform':govtappform}
    return render(request, 'ems/doc.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateUserForm(request, pk):

    user=User.objects.get(id=pk)
    userform = userForm(instance=user)

    if request.method == 'POST':
        userform = userForm(request.POST, instance=user)

        if userform.is_valid():
            userform.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated, {} {}'.format(
                request.user, user.last_name,user.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[user.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
            # messages.error(request, ('please go back and correct the error'))

    context = {'userform':userform}
    return render(request, 'staff/updateUser.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def removeStaff(request, pk):
    user=User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'successful deleted: {}'.format(user.last_name))
        return HttpResponseRedirect(reverse('staff:staffhome'))
    context = {'user': user}
    return render(request, 'staff/remove.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateProfileForm(request, pk):

    user=User.objects.get(id=pk)

    profileform = PersonalDetailForm(instance=user.personaldetail)

    if request.method == 'POST':
        profileform = PersonalDetailForm(request.POST, instance=user.personaldetail)

        if profileform.is_valid():
            profileform.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated, {} {}'.format(
                request.user, user.last_name,user.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[user.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'profileform':profileform}
    return render(request, 'staff/updateProfile.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateQualForm(request, pk):

    user=User.objects.get(id=pk)
    qualform = QualForm(instance=user.qualification)

    if request.method == 'POST':
        qualform = QualForm(request.POST, instance=user.qualification)

        if qualform.is_valid():
            qualform.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated, {} {}'.format(
                request.user, user.last_name,user.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[user.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'qualform':qualform}
    return render(request, 'staff/updateQual.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateProQualForm(request, pk):

    user=User.objects.get(id=pk)
    proqualform = ProQualForm(instance=user.professionalqualification)

    if request.method == 'POST':
        proqualform = ProQualForm(request.POST, instance=user.professionalqualification)

        if proqualform.is_valid():
            proqualform.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated, {} {}'.format(
                request.user, user.last_name,user.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[user.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'proqualform':proqualform}
    return render(request, 'staff/updateProQual.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateGovtAppForm(request, pk):

    user=User.objects.get(id=pk)
    govtappform = GovtAppForm(instance=user.governmentappointment)
    if request.method == 'POST':
        govtappform = GovtAppForm(request.POST, instance=user.governmentappointment)

        if govtappform.is_valid():
            
            govtappform.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated, {} {}'.format(request.user, user.last_name,user.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[user.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'govtappform':govtappform,'user':user}
    return render(request, 'staff/updateGovtApp.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def promotion(request,pk):
    PromoFormSet=inlineformset_factory(User,Promotion,fields=('current_post','promotion_date','grade_level','step','incremented_date','confirmation_date',),extra=1,can_delete=False)
    emp=User.objects.get(id=pk)
    formset=PromoFormSet(queryset=Promotion.objects.none(),instance=emp)
    
    if request.method == 'POST': 
        formset = PromoFormSet(request.POST,instance=emp)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful added promotion for: {}'.format(emp.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[emp.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'formset':formset}
    return render(request, 'staff/promotion.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatePromotion(request, pk):
    emp=Promotion.objects.get(id=pk)
    
    formset = PromotionForm(instance=emp)
 
    if request.method == 'POST':
        formset = PromotionForm(request.POST, instance=emp)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful updated promotion for: {}'.format(emp.emp.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[emp.emp.id])
                return HttpResponseRedirect(staff_details_url)
        # # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'formset':formset, 'emp':emp}
    return render(request, 'staff/promotion.html', context)



@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def removePromotion(request, pk):
    user=Promotion.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'successful deleted promotion for: {}'.format(user.emp.last_name))
        staff_details_url=reverse('staff:staffdetail', args=[user.id])
        return HttpResponseRedirect(staff_details_url)
    context = {'user': user}
    return render(request, 'staff/removePromotion.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def discipline(request,pk):
    DisFormSet=inlineformset_factory(User, Discipline, fields=('offense', 'decision','date', 'comment'),extra=1, can_delete=False)
    dis=User.objects.get(id=pk)
    formset=DisFormSet(queryset=Discipline.objects.none(),instance=dis)
    # disciplineform = DisciplineForm(initial={'emp':dis})

    if request.method == 'POST': 
        formset = DisFormSet(request.POST,instance=dis)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful added discipline for: {}'.format(dis.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[dis.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))
        
    context = {'formset':formset}
    # context = {'disciplineform':disciplineform}
    return render(request, 'staff/discipline.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateDiscipline(request, pk):
    dis=Discipline.objects.get(id=pk)
    # disciplineform = DisciplineForm(instance=dis)
    formset = DisciplineForm(instance=dis)
 
    if request.method == 'POST':
        # disciplineform = DisciplineForm(request.POST, instance=dis)
        formset = DisciplineForm(request.POST, instance=dis)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful updated discipline for: {}'.format(dis.emp.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[dis.emp.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'formset':formset, 'dis':dis}
    return render(request, 'staff/discipline.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def removeDiscipline(request, pk):
    user=Discipline.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'successful deleted dicipline for: {}'.format(user.emp.last_name))
        staff_details_url=reverse('staff:staffdetail', args=[user.id])
        return HttpResponseRedirect(staff_details_url)
    context = {'user': user}
    return render(request, 'staff/removeDiscipline.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def leave(request,pk):
    LeaveFormSet=inlineformset_factory(User, Leave,fields=('nature_of_leave','year','start_date','number_of_days_granted','total_days','status','comment_if_any'), extra=1, can_delete=False)
    leave=User.objects.get(id=pk)
    formset=LeaveFormSet(queryset=Leave.objects.none(),instance=leave)
    users=leave

    lev=users.leave_set.last()

    if request.method == 'POST': 
        formset = LeaveFormSet(request.POST,instance=leave)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.clean()  # Trigger the model's clean() m
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful created leave for: {}'.format(leave.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[leave.id])
                return HttpResponseRedirect(staff_details_url)
        else:
            # # raise ValidationError('bad entry')
            # messages.error(request, ('please go back and correct the error'))
            # formset = LeaveFormSet()
            formset = LeaveFormSet(request.POST,instance=leave)

    context = {'formset':formset,'lev':lev}
    return render(request, 'staff/leave.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateLeave(request, pk):
    
    leave=Leave.objects.get(id=pk)
    formset = LeaveForm(instance=leave)
 
    if request.method == 'POST':
        formset = LeaveForm(request.POST, instance=leave)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful updated leave for: {}'.format(leave.emp.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[leave.emp.id])
                return HttpResponseRedirect(staff_details_url)     
            # else:
        #     messages.error(request, ('please go back and correct the error'))
    

    context = {'formset':formset, 'leave':leave}
    return render(request, 'staff/leave.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def removeLeave(request, pk):
    user=Leave.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'successful deleted leave for: {}'.format(user.emp.last_name))
        staff_details_url=reverse('staff:staffdetail', args=[user.id])
        return HttpResponseRedirect(staff_details_url)
    
    context = {'user': user}
    return render(request, 'staff/removeLeave.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def execapp(request,pk):
    ExecFormSet=inlineformset_factory(User, ExecutiveAppointment,fields=('designation_post','date_of_appointment','status_current_out_of_office'),extra=1, can_delete=False)
    execapp=User.objects.get(id=pk)
    formset=ExecFormSet(queryset=ExecutiveAppointment.objects.none(),instance=execapp)
    # execappform = ExecutiveAppForm(initial={'emp':execapp})
    
    if request.method == 'POST': 
        formset = ExecFormSet(request.POST,instance=execapp)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful created executive apppointment for: {}'.format(execapp.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[execapp.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))

    context = {'formset':formset}
    return render(request, 'staff/execapp.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateExecApp(request, pk):

    execapp=ExecutiveAppointment.objects.get(id=pk)
    formset = ExecutiveAppForm(instance=execapp)
 
    if request.method == 'POST':
        formset = ExecutiveAppForm(request.POST, instance=execapp)

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful updated executive appointment for: {}'.format(execapp.emp.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[execapp.emp.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))
    
    context = {'formset':formset, 'execapp':execapp}
    return render(request, 'staff/execapp.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def removeExecApp(request, pk):
    user=ExecutiveAppointment.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'successful deleted executive appointment for: {}'.format(user.emp.last_name))
        staff_details_url=reverse('staff:staffdetail', args=[user.id])
        return HttpResponseRedirect(staff_details_url)
    
    context = {'user': user}
    return render(request, 'staff/removeexecapp.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def retirement(request,pk):
    RetireFormSet=inlineformset_factory(User, Retirement,fields=('date_retired','status'),extra=1, can_delete=False)
    retire=User.objects.get(id=pk)
    formset=RetireFormSet(queryset=Retirement.objects.none(),instance=retire)
   
    if request.method == 'POST':
        formset = RetireFormSet(request.POST,instance=retire)
        

        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, 'successful completed retirement for: {}'.format(retire.last_name))
                staff_details_url=reverse('staff:staffdetail', args=[retire.id])
                return HttpResponseRedirect(staff_details_url)
    
    context = {'formset':formset}
    return render(request, 'staff/retire.html', context)
    

@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def updateRetirement(request, pk):

    retire=Retirement.objects.get(id=pk)
    formset = RetirementForm(instance=retire)

    if request.method == 'POST':
        formset = RetirementForm(request.POST, instance=retire)
        
        if formset.is_valid():
            formset.save()
            if request.user.is_superuser:
                messages.success(request, '{} successful updated retirement for: {} {}'.format(
                request.user, retire.emp.last_name,retire.emp.first_name))
                staff_details_url=reverse('staff:staffdetail', args=[retire.emp.id])
                return HttpResponseRedirect(staff_details_url)
        # else:
        #     messages.error(request, ('please go back and correct the error'))


    context = {'formset':formset, 'retire':retire}
    return render(request, 'staff/retire.html', context)


@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def removeRetire(request, pk):
    user=Retirement.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'successful deleted retirement entry for: {}'.format(user.emp.last_name))
        staff_details_url=reverse('staff:staffdetail', args=[user.id])
        return HttpResponseRedirect(staff_details_url)
    context = {'user': user}
    return render(request, 'staff/removeretire.html', context)
