from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Student_Info_Form, Student_Contact_Form, Student_Course_Form
from .models import Student_Info_Model, Student_Contact_Model, Student_Course_Model
# Create your views here.

@login_required
def  home(request):
    return render(request,'home/home.html')

@login_required
def addmission_view(request):
    objinfo =  Student_Info_Form()
    objcontact = Student_Contact_Form()
    objcourse = Student_Course_Form()

    return render(request,'addmission/addmission.html',{'msginfo':objinfo, "msgcontact":objcontact, "msgcourse":objcourse})

@login_required
def addmission_status_view(request):
    return render(request,'addmission/addmission_status.html')

@login_required
def add_student(request):
    try:
        if request.method == 'POST':
            objstudent_info = Student_Info_Form(request.POST, request.FILES)
            objstudent_contact = Student_Contact_Form(request.POST)
            objstudent_course = Student_Course_Form(request.POST)

            if objstudent_info.is_valid() and objstudent_contact.is_valid() and objstudent_course.is_valid():
                # Save the student info first
                student_info = objstudent_info.save()

                # Now create the contact and course instances, linking to the student
                contact = objstudent_contact.save(commit=False)
                contact.student = student_info  # Set the foreign key
                contact.save()

                course = objstudent_course.save(commit=False)
                course.student = student_info  # Set the foreign key
                course.save()

                return render(request, 'addmission/addmission.html', {
                    'msgadd': 'Added Successfully, please Note your Student id ' + str(student_info.id)
                })
            else:
                # If forms are not valid, pass the errors to the template
                return render(request, 'addmission/addmission.html', {
                    'msgadd_error': 'Unsuccessful, please check the details you have entered',
                    'errors': {
                        'info_errors': objstudent_info.errors,
                        'contact_errors': objstudent_contact.errors,
                        'course_errors': objstudent_course.errors
                    }
                })
        else:
            return render(request, 'addmission/addmission.html')
    except Exception as e:
        return render(request, 'addmission/addmission.html', {
            'msgadd_error': 'An unexpected error occurred: ' + str(e)
        })

@login_required
def student_status(request):
    try:
        student_id = request.POST.get('student_id')  
        obj_std = Student_Info_Model.objects.get(id=student_id)
        return render(request, 'addmission/addmission_status.html', {'msg': {obj_std}}) 
    except Exception as e:
        return render(request, 'addmission/addmission_status.html', {'errormsg': 'Student ID not found'})

@login_required
def student_display(request):
    try:
        student_dis = request.POST.get('student_dis')  
        obj_info = Student_Info_Model.objects.get(id=student_dis)
        obj_contact = Student_Contact_Model.objects.get(id=student_dis)
        obj_course= Student_Course_Model.objects.get(id=student_dis)
        return render(request, 'addmission/addmission_status.html', {'msg_info': {obj_info}, "msg_contact": {obj_contact}, "msg_course": {obj_course}})  
    except Exception as e:
        return render(request, 'addmission/addmission_status.html', {'msg_info_error': 'student not found'})