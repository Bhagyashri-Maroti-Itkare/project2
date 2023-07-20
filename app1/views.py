from django.shortcuts import render

# Create your views here.
from .forms import singupform1
from django.contrib import messages

# sign_up sathi
def sign_up1(request):
    if request.method == 'POST':
        fm = singupform1(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully !!')
            fm.save()
            fm = singupform1()
    else:
        fm = singupform1()
    return render(request, 'app1/f12.html', {'form': fm})

# login sathi
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data= request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/aa/get14/')
    else:
        fm = AuthenticationForm()

    return render(request,'app1/f13.html',{'form':fm})

# profile 

from .forms import edit_user_profile_form

def user_profile(request):
    #if request.user.is_authenticated:
    fm = edit_user_profile_form(instance=request.user)
    return render(request,'app1/f14.html',{'name':request.user,'form':fm})

# logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/aa/get13')

# Cookies

# set cookies
def setcookies(request):
    response = render(request,'app1/f15.html')
    response.set_cookie("name","shri",max_age=60) # cookie set krt astna max_age pn write krau shkto (60 min timming sathi)
    return 

'''# or
from datetime import datetime,timedelta

def setcookies(request):
    response = render(request,'app1/f15.html')
    response.set_cookie("name","shri",expires=datetime.utcnow()+timedelta(days=2)) # 2 days na cookie expire hote
    return reaponse
'''
# get cookies
def getcookies(request):
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name)
    nm = request.COOKIES['name']
    return render(request,'app1/f16.html',{'name':nm})

# Delete Cookies
def deletecookies(request):
    response = render(request,'app1/f17.html')
    response.delete_cookie('name')
    return response

# session

def setsession(request):
    request.session['name'] = 'Shri'
    request.session['lname'] = 'Radha'
    #request.session.set_expiry(600)
    return render(request,'app1/f18.html')

from django.http import HttpResponse
def getsession(request):
    if 'name' in request.session:
    #name = request.session['name] or
        name = request.session.get('name',default='gust')
        lname = request.session.get('lname')
        request.session.modified = True
        return render(request,'app1/f19.html',{'name':name,'lname':lname})
    else:
        return HttpResponse("Your session has expired")
    
    '''
    STATIC_URL = 'static/'
    SESSION_COOKIE_AGE = 10
    '''

def get_key(request):
    name = request.session.get('name')
    keys = request.session.keys()
    #age = request.session.setdefault('age','25')
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request,'app1/f20.html',{'name':name,'key':keys,'item':items})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        #request.session.flush()
        return render(request,'app1/f21.html')
    

def setsession1(request):
    request.session['name'] = 'Shri'
    request.session['lname'] = 'Radha'
    return render(request,'app1/f22.html')

def getsession1(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    return render(request,'app1/f23.html',{'name':name,'lname':lname})

def delsession1(request):
    request.session.flush()
    return render(request,'app1/f24.html')

# page counter project
def home(request):
    ct = request.session.get('count',0)
    newcount = ct + 1
    request.session['count'] = newcount
    return render(request,'app1/f25.html',{'c':newcount})



