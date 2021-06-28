from django.http.response import HttpResponseRedirect
from project.models import Contact
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')

@csrf_exempt
def add_contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']

        contact = Contact(fname=fname, lname = lname, email = email, phone=phone, address=address, address2=address2,city=city, state=state, zip=zip)
        contact.save()
        messages.info(request, 'Contact Entered')
        return redirect('contacts')
    

@csrf_exempt
def delete_contact(request, id):
    Contact.objects.get(id=id).delete()
    return HttpResponseRedirect("/")

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username not available')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists in DB')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password = password, email = email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'Account created')
                return redirect('login')
        else:
            messages.info(request, 'Password and Confirmed password do not match.')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')

@csrf_exempt
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html',{
        "contacts": contacts
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    
    return render(request,'search.html')
