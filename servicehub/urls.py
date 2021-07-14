"""servicehub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from serviceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #common urls
    path('index/', views.index),
    path('', views.index),
    path('login/', views.login),   
    path('userreg/', views.userreg),
    path('screg/', views.screg),



    #user
    path('userhome/', views.userhome),
    path('booking/', views.booking),
    path('feedback/', views.feedback),
    # path('addquestion/', views.addquestion),
    path('addquestionsc/', views.addquestionandanswer),
    path('search/', views.searchforsc),
    path('searchdisplay/', views.searchdisplay),
    path('viewquestion/', views.viewquestion),
    path('gallery/', views.gallery),
    path('problem/', views.wtsurproblem),
    path('viewanswers/', views.viewanswers),
    path('viewstatusbyuser/', views.viewstatusbyuser),
    path('feedbackpreview/', views.feedbackpreview),
    path('feedback/', views.feedback),
    path('viewfeedbackbysc/', views.viewfeedbackbysc),
    path('viewfaq/', views.viewfaq),
    path('useraddmessage/', views.useraddmessage),
    path('userviewmessage/', views.userviewmessage),







    #admin url
    path('adminhome/', views.adminhome),
    path('addcompany/', views.addcompany),
    path('approvesc/', views.approvesc),
    path('viewfeedbackbyadmin/', views.viewfeedbackbyadmin),
    path('adminaddmessage/', views.adminaddmessage),
    path('adminviewmessage/', views.adminviewmessage),
    



    #sc
    path('viewbooking/', views.viewbooking),
    path('schome/', views.schome),
    path('updatebookingstatus/', views.updatebookingstatus),
    path('faq/', views.faq),
    path('scaddmessage/', views.scaddmessage),
    path('scviewmessage/', views.scviewmessage),
    path('viewupcomings/', views.viewupcomings),
    path('scviewprofile/', views.scviewprofile),


    
]
