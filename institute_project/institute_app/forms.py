from .models import Student_Info_Model, Student_Contact_Model, Student_Course_Model
from django import forms

class Student_Info_Form(forms.ModelForm):
    class Meta:
        model = Student_Info_Model
        fields = ['first_name', 'middle_name', 'surname', 'gender', 'dob','image']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }


class Student_Contact_Form(forms.ModelForm):
    class Meta:
        model = Student_Contact_Model
        fields = ['email_id', 'address', 'city', 'state', 'country', 'postal_code', 'mobile_num','aadhaar_number']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'}),
            'mobile_num': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'aadhaar_number': forms.TextInput(attrs={'placeholder': 'Aadhaar Number'})
        }


class Student_Course_Form(forms.ModelForm):
    class Meta:
        model = Student_Course_Model
        fields = ['class_type','course']
        widgets = {
            'course': forms.Select(),
        }
