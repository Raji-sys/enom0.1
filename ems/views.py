from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import *
from .decorators import *
from staff.forms import *
from staff.models import *


@login_required(login_url='ems:login')
def home(request):
    return render(request, 'ems/home.html')


@login_required(login_url='ems:login')
def Auth(request):
    return render(request, 'ems/auth.html')


# @unauthenticated_user
@login_required
def doc(request): 
    if request.method == 'POST':
        userform = userForm(request.POST, instance=request.user)
        profileform = PersonalDetailForm(request.POST, instance=request.user.personaldetail)
        qualform = QualForm(request.POST, instance=request.user.qualification)
        proqualform = ProQualForm(request.POST, instance=request.user.professionalqualification)
        govtappform = GovtAppForm(request.POST, instance=request.user.governmentappointment)
        

        # if userform.is_valid() and profileform.is_valid:
        if userform.is_valid() and profileform.is_valid() and qualform.is_valid() and proqualform.is_valid() and govtappform.is_valid():
            userform.save()
            profileform.save()
            qualform.save()
            proqualform.save()
            govtappform.save()
            messages.success(request, 'documentation was successful {}'.format(request.user.last_name))
            return HttpResponseRedirect(reverse('ems:user'))
        else:
            messages.error(request, ('please correct the error'))
    else:
        userform = userForm(instance=request.user)
        profileform = PersonalDetailForm(request.POST, instance=request.user.personaldetail)
        qualform = QualForm(request.POST, instance=request.user.qualification)
        proqualform = ProQualForm(request.POST, instance=request.user.professionalqualification)
        govtappform = GovtAppForm(request.POST, instance=request.user.governmentappointment)

    context = {'userform':userform,'profileform': profileform, 
               'qualform': qualform,'proqualform':proqualform,
               'govtappform':govtappform,}
    if request.user.personaldetail.staff_no == None:
        return render(request, 'ems/doc.html', context)
    else:
        return HttpResponseRedirect(reverse('ems:user'))


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'account was created for {}'.format(username))
            return HttpResponseRedirect(reverse('staff:staffhome'))

    context = {'form': form}
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('ems:home'))
    else:
        return render(request, 'ems/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('ems:user'))
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(reverse('ems:home'))
    else:
        return render(request, 'ems/login.html', context)


@login_required(login_url='ems:login')
def userPage(request):
    context={}
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('ems:home'))
    else:
        return render(request, 'ems/user.html', context)

def logoutUser(request):
    messages.success(request, 'successful logged out {}'.format(request.user))
    logout(request)
    return HttpResponseRedirect(reverse('ems:login'))