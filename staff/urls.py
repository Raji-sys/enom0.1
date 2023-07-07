from django.urls import path

from . import views 

app_name='staff'

urlpatterns=[
    path('staff/', views.staffView, name='staffhome'),
    path('stats/', views.stats, name='stats'),
    path('report/', views.report, name='report'),
    path('notice/', views.notice, name='notice'),

    path('staff/<int:pk>/', views.staffDetail, name='staffdetail'),


    path('csvFile/', views.csvFile, name='csvfile'),
    path('pdfFile/', views.pdfFile, name='pdffile'),

    path('promotion/<int:pk>/',views.promotion, name='promotionform'),
    path('discipline/<int:pk>/',views.discipline, name='disciplineform'),
    path('leave/<int:pk>/',views.leave, name='leaveform'),
    path('execapp/<int:pk>/',views.execapp, name='execappform'),
    path('retire/<int:pk>/',views.retirement, name='retireform'),
    
    path('updateform/<int:pk>/',views.updateForm, name='updatedocform'),
    path('updateuser/<int:pk>/',views.updateUserForm, name='updateuserform'),
    path('updateprofile/<int:pk>/',views.updateProfileForm, name='updateprofileform'),
    
    path('updatequal/<int:pk>/',views.updateQualForm, name='updatequalform'),
    path('updateproqual/<int:pk>/',views.updateProQualForm, name='updateproqualform'),
    path('updategovtapp/<int:pk>/',views.updateGovtAppForm, name='updategovtappform'),
 
    path('updatepromotion/<int:pk>/',views.updatePromotion, name='updatepromotionform'),
    path('updatediscipline/<int:pk>/',views.updateDiscipline, name='updatedisciplineform'),
    path('updateleave/<int:pk>/',views.updateLeave, name='updateleaveform'),
    path('updateexecapp/<int:pk>/',views.updateExecApp, name='updateexecappform'),
    path('updateretire/<int:pk>/',views.updateRetirement, name='updateretirementform'),
    
    path('removepromotion/<int:pk>/',views.removePromotion, name='removepromotion'),
    path('removediscipline/<int:pk>/',views.removeDiscipline, name='removediscipline'),
    path('removeleave/<int:pk>/',views.removeLeave, name='removeleave'),
    path('removeexecapp/<int:pk>/',views.removeExecApp, name='removeexecapp'),
    path('removeretirement/<int:pk>/',views.removeRetire, name='removeretire'),
    
    path('remove/<int:pk>/',views.removeStaff, name='remove'),
]