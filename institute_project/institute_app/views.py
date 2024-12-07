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
            # Handle the case where the method is not POST (e.g., GET request)
            return render(request, 'addmission/addmission.html')
    except Exception as e:
        # Handle any unforeseen exceptions
        return render(request, 'addmission/addmission.html', {
            'msgadd_error': 'An unexpected error occurred: ' + str(e)
        })