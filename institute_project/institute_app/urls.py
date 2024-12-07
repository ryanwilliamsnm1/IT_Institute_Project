from django.urls import path
from .import views

urlpatterns = [
     path("",views.home ,name='home'),
     path('addmission/',views.addmission_view,name='addmission'),
     path('add/',views.add_student,name='addstudent'),
]