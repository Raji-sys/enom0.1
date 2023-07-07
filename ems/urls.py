from django.urls import path

from .import views 
app_name='ems'

urlpatterns=[
    # path('', HomeView.as_view(), name='home'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home,name='home'),
    path('register/', views.registerPage,name='register'),
    path('doc/', views.doc,name='doc'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user'),
    # path('userdetails/<int:pk>', views.userDetailPage, name='userdetails'),
    path('auth/', views.Auth, name='auth'),
    # path('account',views.accountSettings,name='account'),
]
