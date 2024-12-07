from django.urls import path
from .import views

urlpatterns = [
    path('python/',views.python_course, name= 'python'),
    path('digital/',views.digital_marketing_course, name= 'digital'),
    path('softtest/',views.software_testing_course, name='softtest'),
    path('contact_us/',views.contact, name='contact_us'),
    path('about_us/',views.about, name="about_us")
]