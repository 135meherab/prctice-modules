from django import forms
from . models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'roll': "Student roll",
            'name': "Student Name",
            'email': "Student Email",
            'new': "Is New Student ?",
            'birth_date': "Date of Birth",
            'birth_time': "Time of Birth",
            'form': "Upload Your Application form",
            'img': "Student Image",
            'fee': "Enter Amount of money you want to pay Now",
            'social': "Enter your social media urls",
        }
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'birth_time' : forms.TimeInput(attrs={'type': 'time'}),
        }