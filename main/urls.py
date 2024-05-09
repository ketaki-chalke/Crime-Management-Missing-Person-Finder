from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
   # path('signupA',views.adminSignup, name="signupA"),
   # path('signupG',views.button, name="signupG"),
    path('loginA',views.adminLogin, name="loginA"),
    path('logoutt',views.user_logout,name="logoutt"),
    path('features',views.feat, name="features"),


    path('signupG',views.publicsignup, name="signupG"),
    path('signinG',views.signinG,name="signinG"),
    path('logout',views.LogoutPage,name="logout"),

    
    path('case',views.case,name="case"),

    path('faq.html',views.faq,name="faq"),
    path('faq2.html',views.faq2,name="faq2"),

    path('missing.html',views.missing,name="missing"),
    path('report',views.report,name="report"),
    path('edit.html',views.edit,name="edit"),
    path('delete/<int:case_id>', views.delete_std, name="delete_std"),
    path('update-crime-report/<int:case_id>/',views.update_crime_report,name="update_crime_report"),
    path('uup',views.uPd,name="uPd"),

    path('cr2.html',views.cr2,name="cr2"),
    path('cr1.html',views.cr2,name="cr1"),
    path('contact.html',views.contact,name="contact"),
    
    path('recog',views.recog,name="recog"),
    path('my.html',views.my,name="my")
]


