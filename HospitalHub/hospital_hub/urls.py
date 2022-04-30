"""
Definition of urls for hospital_hub.
"""

from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('logout', views.Logout, name='user_logout'),
    #########################
    # paths for owner

    # example :        path('/Onwer/Hoapitals', views.logowner, name='onwer_login'),
    # example :        path('/Onwer/home', views.index, name='onwer_home'),



    #########################
    # paths for admin
    path('a', views.Admin.AdminLogin, name='admin_login'),

    path('admin', views.Admin.AdminLogin,name='admin_login'),
    path('admin/login', views.Admin.AdminLogin,name='admin_login'),
    path('admin/home', views.Admin.AdminHome,name='admin_home'),
    path('admin/logout', views.Admin.AdminLogout,name='admin_logout'),
    path('admin/add_admin', views.Admin.AddAdmin,name='admin_add_admin'),
    path('admin/add_speciality', views.Admin.AddSpeciality,name='add_speciality'),
    path('admin/add_doctor', views.Admin.AddDoctor,name='add_doctor'),
    path('admin/admins',views.Admin.ViewAdmins,name='admin_view_admins'),
    path('admin/admins/remove/<int:removed_admin_id>',views.Admin.RemoveAdmin,name='remove_admin'),
    path('admin/doctors',views.Admin.ViewDoctors,name='admin_view_doctors'),
    path('admin/doctors/remove/<int:doctor_id>',views.Admin.RemoveDoctorFromDoctors ,name='remove_doctor_from_doctors'),
    path('admin/doctors/<str:doctor>',views.Admin.ViewDoctorProfile,name='admin_view_doctor'),
    path('admin/specialities',views.Admin.ViewSpecialities,name='view_specialities'),
    path('admin/specialities/remove/<int:speciality_id>',views.Admin.RemoveSpeciality,name='remove_speciality'),
    path('admin/specialities/<str:speciality>',views.Admin.ViewSpeciality,name='view_speciality'),
    path('admin/specialities/speciality/remove_doctor/<int:doctor_id>',views.Admin.RemoveDoctorFromSpeciality ,name='remove_doctor_from_speciality'),
    #########################
    # paths for doctor
    path('doctor/register', views.Doctor.DoctorRegister, name='doctor_register'),
    path('doctor/login', views.Doctor.DoctorLogin, name='doctor_login'),
    # displaying schedual and some other data
    path('doctor/home', views.Doctor.DoctorHome, name='doctor_home'),




    #########################
    # paths for patient

    path('patient/login', views.Patient.PatientLogin, name='patient_login'),
    path('patient/register', views.Patient.PatientRegister, name='patient_register'),
    path('patient/home', views.Patient.PatientHome, name='patient_home'),
    
    path('patient/searchbyspeciality', views.Patient.searchbyspeciality, name='specialities_search'),
    path('patient/find_hospitals_by_speciality', views.Patient.find_hospitals_by_speciality, name='find_hospitals_by_speciality'),
]
