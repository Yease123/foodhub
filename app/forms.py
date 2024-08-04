from django import forms

from django.contrib.auth.models import User
import re
class signupasuser(forms.Form):  
    username=forms.CharField( max_length=20, required=True, error_messages={'required': 'Username is required'},widget=forms.EmailInput(attrs={'class':'input'}))
    email=forms.EmailField( max_length=20, required=True, error_messages={'required': 'Email is required'},widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField( required=True, error_messages={'required': 'Password is required'},widget=forms.PasswordInput(attrs={'class':'input'}))
    address=forms.CharField( required=True, error_messages={'required': 'Address is required'},widget=forms.TextInput(attrs={'class':'input'}))
    phone=forms.CharField( required=True, error_messages={'required': 'Phone is required'},widget=forms.NumberInput(attrs={'class':'input'}))
    def clean_username(self):
        data = self.cleaned_data.get("username")
      
        if len(data)<4 or len(data)>20:
            raise forms.ValidationError("username must be between 4 to 20 length")
        if User.objects.filter(username=data):
            raise forms.ValidationError("Username is already taken")
        return data
    def clean_email(self):
        data=self.cleaned_data.get("email")
        email_regex = (
            r'^[a-zA-Z0-9._%+-]+@'
            r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        )
        if not re.match(email_regex, data):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=data):
            raise forms.ValidationError("email is already taken")
        return data
    def clean_password(self):
        data=self.cleaned_data.get("password")
        if len(data)<7 :
            raise forms.ValidationError("Password mustbe of altleast 7 digits")
        return data
    def clean_phone(self):
        data=self.cleaned_data.get("phone")
        if len(data)!=10:
            raise forms.ValidationError("Phone number must be of 10 digit")
        return data
class sigupasresturant(forms.Form):
    username=forms.CharField( max_length=20, required=True, error_messages={'required': 'Username is required'},widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.CharField(  required=True, error_messages={'required': 'Email is required'},widget=forms.EmailInput(attrs={'class':'input'}))
    address=forms.CharField(  required=True, error_messages={'required': 'Address is required'},widget=forms.TextInput(attrs={'class':'input'}))
    logititude=forms.CharField( required=True, error_messages={'required': 'logititude is required'},widget=forms.NumberInput(attrs={'class':'input'}))
    latitude=forms.CharField(  required=True, error_messages={'required': 'latitude is required'},widget=forms.NumberInput(attrs={'class':'input'}))
    phone=forms.CharField( max_length=10, required=True, error_messages={'required': 'Phone is required'},widget=forms.NumberInput(attrs={'class':'input'}))
    opening=forms.CharField( required=True, error_messages={'required': 'Opening hour is required'},widget=forms.TimeInput(attrs={'class':'input'}))
    closing=forms.CharField( required=True, error_messages={'required': 'Closing hour is required'},widget=forms.TimeInput(attrs={'class':'input'}))
    password=forms.CharField(  required=True, error_messages={'required': 'Password  is required'},widget=forms.PasswordInput(attrs={'class':'input'}))
    photo=forms.ImageField(required=True, error_messages={'required': 'photo  is required'},widget=forms.FileInput(attrs={'class':'input'}))
    
    def clean_username(self):
        data=self.cleaned_data.get("username")
        if len(data)<3:
            raise forms.ValidationError("Username length must be greater than 3")
        if User.objects.filter(username=data):
            raise forms.ValidationError("Username is already taken")
        return data
    def clean_email(self):
        data=self.cleaned_data.get("email")
        email_regex = (
            r'^[a-zA-Z0-9._%+-]+@'
            r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        )
        if not re.match(email_regex, data):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=data):
            raise forms.ValidationError("email is already taken")
        return data
    def clean_password(self):
        data=self.cleaned_data.get("password")
        if len(data)<7:
            raise forms.ValidationError("password length must be greater than 7")
        return data
    def clean_phone(self):
        data=self.cleaned_data.get("phone")
        if len(data)!=10:
            raise forms.ValidationError("phone must be of 10 digits")
        return data
   
class signupasdelivery(forms.Form):
    password=forms.CharField(max_length=20, required=True,error_messages={"required":"password is required"},widget=forms.PasswordInput(attrs={'class':'input'}))
    username=forms.CharField(max_length=20, required=True,error_messages={"required":"Username is required"},widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(required=True,error_messages={"required":"Email is required"},widget=forms.EmailInput(attrs={'class':'input'}))
    address=forms.CharField(required=True,error_messages={"required":"address field is required"},widget=forms.TextInput(attrs={"class":"input"}))
    phone=forms.CharField(required=True,error_messages={"required":"phone is required"},widget=forms.NumberInput(attrs={"class":"inpit"}))
    photo=forms.ImageField(required=True,error_messages={"required":"photo is required"},widget=forms.FileInput(attrs={"class":"input"}))
    
    
    def clean_username(self):
        data=self.cleaned_data.get("username")
        if len(data)<3:
            raise forms.ValidationError("Username length must be greater than 3")
        if User.objects.filter(username=data):
            raise forms.ValidationError("Username is already taken")
        return data
    def clean_password(self):
        data=self.cleaned_data.get("password")
        if len(data)<7:
            raise forms.ValidationError("password length must be greater than 7")
        return data
    def clean_email(self):
        data=self.cleaned_data.get("email")
        email_regex = (
            r'^[a-zA-Z0-9._%+-]+@'
            r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        )
        if not re.match(email_regex, data):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=data):
            raise forms.ValidationError("email is already taken")
        return data
    def clean_phone(self):
        data=self.cleaned_data.get("phone")
        if len(data)!=10:
            raise forms.ValidationError("phone must be of 10 digits")
        return data







