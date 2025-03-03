from django import forms
from .models import StudentRegister, StudentContact, StudentChat

class StudentForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Full Name',
        'class' : 'input-field'
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder' : 'Age',
        'class' : 'input-field'
    }))
    studentid = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Student ID',
        'class' : 'input-field'
    }))
    # gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={
    #     'placeholder' : 'Gender'
    # }))
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', widget=forms.Select(attrs={}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Email Address',
        'class' : 'input-field'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Password',
        'class' : 'input-field'
    }))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder' : 'Phone Number',
        'class' : 'input-field'
    }))
    college = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Name Of College',
        'class' : 'input-field'
    }))
    photo = forms.FileField(widget=forms.FileInput(attrs={
        'placeholder' : 'Student Photo',
        'class' : 'input-field'
    }))
    percentage = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder' : 'Marks Percentage',
        'class' : 'input-field'
    }))
    class Meta:
        model = StudentRegister
        fields = ['name', 
                  'age',
                  'gender',
                  'email',
                  'password',
                  'mobile',
                  'studentid',
                  'college',
                  'photo',
                  'percentage']


class ContactForm(forms.ModelForm): 
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Name',
        'class' : 'input-field'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Email Address',
        'class' : 'input-field'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Message',
        'class' : 'input-field'
    }))
    class Meta:
        model = StudentContact
        fields = ['name','email','message']