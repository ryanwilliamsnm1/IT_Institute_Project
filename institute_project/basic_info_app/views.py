from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def python_course(request):
    return render(request,'courses/python.html')

def digital_marketing_course(request):
    return render(request,'courses/digitalmarketing.html')

def software_testing_course(request):
    return render(request,'courses/softtest.html')

def contact(request):
    return render(request,'info-contact/contact_us.html')

def about(request):
    return render(request, 'info-contact/about_us.html')
 