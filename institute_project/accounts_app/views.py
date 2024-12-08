from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import Alter_Signin_Form
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        objlogin = authenticate(username = Username, password = Password)
        if objlogin is not None:
            login(request,objlogin)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request,'registration/login.html',{'msg': 'invalid login', 'form': form})
    else:
        form = AuthenticationForm()
        return render(request,'registration/login.html',{'form': form})

#Logout Function
def logout_view(request):
    logout(request)
    return redirect('login')

#Function for creating new user
def sign_up(request):
    try:
        form = Alter_Signin_Form(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('login')
            return render(request,'authentications/sign_up.html',{'form':form,'msg':"Invalid login"})
        else:
            form = Alter_Signin_Form()
            return render(request, 'authentications/sign_up.html',{'form':form, 'msgerror':'Invalid Submission'})
        
    except Exception as e:
        print(e) 
        form = Alter_Signin_Form()
        return render(request,'authentications/sign_up.html', {'form': form})
    
def resetpassword(request):
    if request.method == 'POST':
        uname = request.POST.get('name')  # Use .get() to avoid the error
        newpass = request.POST.get('password')
        
        try:
            user = User.objects.get(username=uname)
            if user is not None:
                if user.check_password(newpass):
                    return render(request, 'authentications/resetpassword.html', {'msg_error': 'Password can\'t be the same as the old one.'})
                user.set_password(newpass)
                user.save()
                return render(request, 'authentications/resetpassword.html', {'msg': 'Password reset successfully'})
        
        except Exception as e:
            print(e)
            return render(request, 'authentications/resetpassword.html', {'msg_error': 'Password reset failed'})
    
    return render(request, 'authentications/resetpassword.html')  # Render the page for GET requests