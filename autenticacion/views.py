from django.shortcuts import render,redirect
from django.views.generic import View 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout , authenticate
from .forms import UserCreationForm

def loginView(request):   
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user=authenticate(username=user_name,password=password)    
            if user is not None:
                login(request,user)
                messages.success(request,F"Bievenido de nuevo {user_name}")                   
                return redirect("productList")
            else:
                messages.error(request,"Los datos son incorrectos")
        else:
            messages.error(request,"Los datos son incorrectos")
    form = AuthenticationForm()       
    return render(request,"autentication/access.html",{"accessForm":form})

class registerView(View):

    def get(self, request):
        form = UserCreationForm()       
        return render(request,"autentication/register.html",{"registerForm":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get("username")
            messages.success(request, F"Registro completado, bienvenido {user_name}")
            login(request, user)
            return redirect("productList")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,"autentication/register.html",{"registerForm":form})

def logoutView(request):
    logout(request)
    messages.success(request, F"Tu sesión se cerró exitosamente.")
    return redirect("login")