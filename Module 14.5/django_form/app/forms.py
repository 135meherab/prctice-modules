from django import forms 
from django.forms.widgets import NumberInput
import datetime
class contactform(forms.Form):
    name = forms.CharField(label="Please Enter your user name", initial="your name", max_length= 15, min_length=5, required= False, help_text="at least 5 characters maximum 15 characters")
    image = forms.FileField()


    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    discription= forms.CharField(widget=forms.Textarea)


    colors = [
        ('blue','Blue'),
        ('red', 'Red'),
        ('green', 'Green')
    ]
    choice = forms.ChoiceField(label="Choose your favorite color", choices=colors)
    choice2 = forms.MultipleChoiceField(label="Choose your Multiple", choices=colors)
    choice3 = forms.ChoiceField(widget=forms.RadioSelect,label="Choose your favorite color with radio select", choices=colors)
    choice4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Choose your Multiple colors with check box", choices=colors)
    
    email = forms.EmailField(label="Enter your user Email")
    password = forms.CharField(widget=forms.PasswordInput,label="Enter your user Password", min_length= 8)

    agree = forms.BooleanField(label = "Agree with terms  and conditions", initial=True)

    bd = forms.DateField(label="Date of Birth",widget=NumberInput(attrs = {'type' : 'date'}), required= False,  initial=datetime.date.today)
    year = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
    join = forms.DateField(label="Date of join", widget=forms.SelectDateWidget(years= year))

    value = forms.DecimalField()
    age = forms.IntegerField(label="Age")  

