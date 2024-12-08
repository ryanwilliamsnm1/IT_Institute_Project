from django.urls import path
from .import views

urlpatterns = [
     path("",views.home ,name='home'),
     path('addmission/',views.addmission_view,name='addmission'),
     path('add/',views.add_student,name='addstudent'),
     path('addmission_status/',views.student_status,name='addmission_status'),
     path('addmission_display/',views.student_display,name='addmission_display'),
     path('status_view/',views.addmission_status_view, name='status_view')
]