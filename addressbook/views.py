from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import UserProfile, ContactInfo
from .forms import LoginForm, RegisterForm, ContactInfoForm


def register(request):
        registered = False
        if request.method == 'POST':
            pform = RegisterForm(request.POST)
            if pform.is_valid():
                user = UserProfile()
                user.username = pform.cleaned_data['emailaddress']
                user.password = pform.cleaned_data['password1']
                user.save()
                return render(request, 'mainpage.html')
            else:
                    print  pform.errors
                    return redirect('/')
        else:
            return redirect('/')
    
def user_login(request):
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = UserProfile.objects.get(username=username, password=password)
          if user is not None:
              request.session['username'] = username
              return render(request, 'mainpage.html')
          else:
              return redirect('/')
    else:
        # the login is a  GET request, so just show the user the login form.
        return redirect('/')

def homepage(request):
    return render(request, 'home.html')

def mainpage(request):
    return render(request, 'mainpage.html')


def logout(request):
    request.session['username'] = None
    return redirect('/')

def create(request):
    
    if not request.session.get('username', None):
        return redirect('/')
    
    if request.method == 'POST':
        contactform = ContactInfoForm(request.POST)
        if contactform.is_valid():
            cinfo = ContactInfo()
            cinfo.firstname = contactform.cleaned_data['firstname']
            cinfo.lastname = contactform.cleaned_data['lastname']
            cinfo.phonenumber = contactform.cleaned_data['phonenumber']
            cinfo.street = contactform.cleaned_data['street']
            cinfo.email = contactform.cleaned_data['email']
            cinfo.save()
            return redirect('/view/')
    else:
        return render(request, 'create.html')

    return render(request, 'mainpage.html')

def deletecontact(request, userid):

    if not request.session.get('username', None):
        return redirect('/')
    if request.method == 'GET':
        if userid:
            try:
                ContactInfo.objects.filter(id=userid).delete()
            except:
                return render(request, 'mainpage.html')
            return redirect('/view/')
    else:
        return render(request, 'mainpage.html')
    
            
def search(request):
    
    if not request.session.get('username', None):
        return redirect('/')

    first_name = request.POST.get('firstname')
    if first_name:    
        contacts = ContactInfo.objects.filter(firstname__contains=first_name)
        return render(request, 'view.html', {'contacts': contacts})
    else:
        return render(request, 'search.html')

def view_contact(request):
    if not request.session.get('username', None):
        return redirect('/')
    
    contacts = ContactInfo.objects.order_by('id')
    return render(request, 'view.html', {'contacts': contacts})