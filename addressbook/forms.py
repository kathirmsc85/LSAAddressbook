from django import forms

            
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

            
class RegisterForm(forms.Form):
    emailaddress = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    
class ContactInfoForm(forms.Form):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    phonenumber = forms.CharField(required=True)
    street = forms.CharField(required=True)
    email = forms.CharField(required=True)