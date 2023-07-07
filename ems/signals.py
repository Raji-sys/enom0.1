from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from staff.models import *
from django.dispatch import receiver
from datetime import date, timedelta


@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='employee')
        instance.groups.add(group)
        PersonalDetail.objects.create(user=instance)
        Qualification.objects.create(user=instance)
        ProfessionalQualification.objects.create(user=instance)
        GovernmentAppointment.objects.create(user=instance)


        
@receiver(post_save,sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.personaldetail.save()
        instance.qualification.save()
        instance.professionalqualification.save()
        instance.governmentappointment.save()

