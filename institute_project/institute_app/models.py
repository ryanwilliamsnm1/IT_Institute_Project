from django.db import models
from django.core.validators import RegexValidator
from .validators import validate_postal_code

# Create your models here.

# STUDENTS BASIC INFORMATIONS

class Student_Info_Model(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="First Name")
    middle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Middle Name")
    surname = models.CharField(max_length=20, null=True, blank=True, verbose_name="Surname")
    
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES, 
        null=False,
        blank=False
    )
    
    dob = models.DateField()
    image = models.ImageField(upload_to='images',default=None,null=True)

    def __str__(self):
        return f"{self.first_name}"
    class Meta:
        db_table = 'student_info'

# STUDENTS CONTACT DETAILS

class Student_Contact_Model(models.Model):

    email_id = models.EmailField(max_length=250, null=False, blank=False, verbose_name="Email Id")
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name='Address')
    city = models.CharField(max_length=100, null=False, blank=False, verbose_name="City")
    state = models.CharField(max_length=100, null=False, blank=False, verbose_name="State")
    country = models.CharField(max_length=100, null=False, blank=False)
    
    postal_code = models.CharField(
        max_length=20, 
        null=False, 
        blank=False, 
        verbose_name="Postal Code",
        validators=[validate_postal_code]
    )
    
    mobile_num = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        validators=[
            RegexValidator(
                regex=r'^\+91[789]\d{9}$|^[789]\d{9}$', 
                message="Mobile number must be entered in the format: '9999999999' or '+919999999999'."
            )
        ]
    )
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    student = models.ForeignKey(Student_Info_Model, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student}"
    
    class Meta:
        db_table = "student_contact"
    

# STUDENTS COURSE RELATED DETAILS

class Student_Course_Model(models.Model):
    id = models.AutoField(primary_key=True)

    TYPE = [
        ('Select', 'select'),
        ('Online', 'online'),
        ('Offline', 'offline')
    ]

    COURSES = [
         ('Select', 'select'),
        ('Python', 'Python'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Software Testing', 'Software Testing'),  
    ]
    class_type = models.CharField(max_length=100,blank=False,null=False,choices=TYPE, default=COURSES)
    course = models.CharField(max_length=100, blank=False, null=False, choices=COURSES, default=TYPE)

    student = models.ForeignKey(Student_Info_Model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student}"
    
    class Meta:
        db_table = 'Course_details'