from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','field_of_study','institution','bio','profile_photo',
                  'last_job', 'company','start_date', 'end_date',
                  )
        
        widgets = {
            'date_of_birth' : forms.DateInput(
                format=('%m/%d/%Y'),
                attrs= {'class':'form-control', 'placeholder':'Select Date', 'type':'date'}), 
            'start_date' : forms.DateInput(
                format=('%m/%d/%Y'),
                attrs= {'class':'form-control', 'placeholder':'Select Date', 'type':'date'}), 
            'end_date' : forms.DateInput(
                format=('%m/%d/%Y'),
                attrs= {'class':'form-control', 'placeholder':'Select Date', 'type':'date'}), 
        }