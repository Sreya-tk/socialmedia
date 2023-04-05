from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User



# Create your views here.
# class MainHome(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"main_home.html")

class MainHome(TemplateView):
    template_name="main_home.html"
    
# class RegView(View):
#     def get(self,request,*args,**kwargs):
#         f=RegForm()
#         return render(request,"reg.html",{"form":f}) 
#     def post(self,request,*args,**kwargs):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User Registration Successfull")
#             return redirect("h")
#         else:
#             messages.error(request,"Registration Failed!")
#             return render(request,"reg.html",{"form":form_data})

class RegView(CreateView):
    form_class=RegForm
    template_name="reg.html"
    model=User
    success_url=reverse_lazy("h")


        
class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    # def get(self,request,*args,**kwargs):
    #     f=LogForm()
    #     return render(request,"log.html",{"form":f}) 
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=ps)
            if user:
                login(request,user)
                messages.success(request,"Login Successfull")
                return redirect("uh")
            else:
                messages.error(request,"incorrect username or password!")
                return render(request,"log.html",{"form":form_data})
        else:
                messages.error(request,"Login Failed!")
                return render(request,"log.html",{"form":form_data})    
            
             