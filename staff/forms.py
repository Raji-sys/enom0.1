from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import inlineformset_factory
from django.forms import BaseFormSet

class PersonalDetailForm(forms.ModelForm):    
    def clean_date_of_birth(self):
        date_of_birth=self.cleaned_data.get('date_of_birth')
        if self.instance.date_of_birth and date_of_birth != self.instance.date_of_birth:
            raise forms.ValidationError('this action is forbidden, {} is the default'.format(self.instance.date_of_birth.strftime("%m-%d-%Y")))
        return date_of_birth

    class Meta:
        model = PersonalDetail
        fields = '__all__'
        exclude = ['user']


class QualForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'
        exclude = ['user']


class ProQualForm(forms.ModelForm):
    class Meta:
        model = ProfessionalQualification
        fields = '__all__'
        exclude = ['user']


class GovtAppForm(forms.ModelForm):
    def clean_date_of_first_appointment(self):
        date_of_first_appointment = self.cleaned_data.get('date_of_first_appointment')
        if self.instance.date_of_first_appointment and date_of_first_appointment != self.instance.date_of_first_appointment:
            raise forms.ValidationError(f'this action is forbidden, {self.instance.date_of_first_appointment.strftime("%m-%d-%Y")} is the default ')
        return date_of_first_appointment
    
    class Meta:
        model = GovernmentAppointment
        fields = '__all__'
        exclude = ['user']


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = '__all__'
        exclude = ['emp']


class DisciplineForm(forms.ModelForm):        
    # date=forms.DateField(
    #     widget=forms.DateInput(format='%d.%m.%Y'), input_formats=['%d.%m.%Y'])
    
    class Meta:
        model = Discipline
        fields = '__all__'
        exclude = ['emp']


class LeaveForm(forms.ModelForm):
    # def clean(self):
    #     cleaned_data = super().clean()
    #     total_days = cleaned_data.get('total_days')
    #     number_of_days_granted = cleaned_data.get('number_of_days_granted')
    #     remain = total_days - number_of_days_granted

    #     if remain < 0 or remain != cleaned_data.get('remain') or remain != total_days:
    #         raise forms.ValidationError('Invalid remaining days value. Please adjust the values.')

    #     return cleaned_data
    
    class Meta:
        model = Leave
        fields = '__all__'
        exclude = ['emp']


class ExecutiveAppForm(forms.ModelForm):
    class Meta:
        model = ExecutiveAppointment
        fields = '__all__'
        exclude = ['emp']


class RetirementForm(forms.ModelForm):
    class Meta:
        model = Retirement
        fields = '__all__'
        exclude = ['emp']

    
    # def __init__(self, *args, **kwargs):
    #     super(RetirementForm,self).__init__(*args, **kwargs)
    #     instance=getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['emp'].widget.attrs['readonly']=True
        
    # def clean_emp(self):
    #     instance=getattr(self,'instance',None)
    #     if instance and instance.pk:
    #         return instance.emp
    #     else:
    #         return self.cleaned_data['emp']