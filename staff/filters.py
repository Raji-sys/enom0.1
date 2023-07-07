import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter, BooleanFilter
from .models import *


class StaffFilter(django_filters.FilterSet):
    # surname=CharFilter(label="surname",field_name='last_name',lookup_expr='icontains' )
    staff_no=CharFilter(label='FILE NO', field_name='personaldetail__staff_no')
    # ippis=CharFilter(label='ippis',field_name='governmentappointment__ippis')
    # date_of_first_appointment=DateFilter(label="date",field_name="governmentappointment__date_of_first_appointment",lookup_expr='exact')

    class Meta:
        model = User
        exclude=['first_name','password','date_joined','last_login','superuser_status','groups',
                 'user_permissions','email','last_name','username','is_superuser','is_active','is_staff']

class GovFilter(django_filters.FilterSet):
    # sdate_of_first_appointment=DateFilter(label="sdate",field_name="governmentappointment__date_of_first_appointment",lookup_expr='lte')
    # edate_of_first_appointment=DateFilter(label="edate",field_name="governmentappointment__date_of_first_appointment",lookup_expr='gte')
    syear_of_appointment=NumberFilter(label="START",field_name="governmentappointment__date_of_first_appointment__year",lookup_expr='lte')
    eyear_of_appointment=NumberFilter(label="END",field_name="governmentappointment__date_of_first_appointment__year",lookup_expr='gt')
    year_of_appointment=NumberFilter(label="YEAR",field_name="governmentappointment__date_of_first_appointment__year",lookup_expr='exact')
    dep=CharFilter(label="DEPT",field_name="governmentappointment__department",lookup_expr='iexact')

    cadre=CharFilter(label="CADRE",field_name="governmentappointment__current_post",lookup_expr='iexact')
  
    state=CharFilter(label="STATE",field_name="personaldetail__state",lookup_expr='iexact')
    lga=CharFilter(label="LGA",field_name="personaldetail__lga",lookup_expr='iexact')
  
    type_of_cadre=CharFilter(label="TYPE",field_name="governmentappointment__type_of_cadre",lookup_expr='iexact')
    due=CharFilter(label="DUE",field_name="governmentappointment__due",lookup_expr='iexact')
  
    rt=CharFilter(label="RETIRE",field_name="governmentappointment__retire",lookup_expr="iexact")
    
    class Meta:
        model = User
        exclude=['first_name','password','date_joined','last_login','superuser_status','groups',
                 'user_permissions','email','last_name','username','is_superuser','is_active','is_staff']


