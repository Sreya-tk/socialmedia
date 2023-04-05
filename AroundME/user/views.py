from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout

# Create your views here.
class UserHome(CreateView):
        template_name="userhome.html"
        form_class=PostForm
        model=Posts
        success_url=reverse_lazy("uh")
        def form_valid(self, form):
                form.instance.user=self.request.user
                self.object=form.save()
                messages.success(self.request,"Post uploaded")
                return super().form_valid(form)
        def get_context_data(self, **kwargs):
                context=super().get_context_data(**kwargs)
                context["data"]=Posts.objects.all().order_by('-datetime')
                context["cform"]=CommentForm()
                context["comments"]=Comments.objects.all()             
                return context
        
        
class ProfileView(TemplateView):
        template_name=("profile.html")      
        
class BioView(CreateView):
        form_class=BioForm
        template_name="bio.html"
        model=Bio
        success_url=reverse_lazy("pro")
        def form_valid(self, form):
                form.instance.user=self.request.user
                self.object=form.save()
                messages.success(self.request,"Bio Added")
                return super().form_valid(form)
              
class EditBioView(UpdateView):
        form_class=BioForm
        template_name="editbio.html"
        model=Bio
        success_url=reverse_lazy("pro")  
        pk_url_kwarg="pk"  
        
class ChangePasswordView(FormView): 
        template_name="changepassword.html"
        form_class=ChangePasswordForm
        def post(self,request,*args,**kwargs):
                
                form_data=ChangePasswordForm(data=request.POST)
                if form_data.is_valid():
                        current=form_data.cleaned_data.get("c_password")
                        new=form_data.cleaned_data.get("n_password")
                        confirm=form_data.cleaned_data.get("conf_password")
                        user=authenticate(request,username=request.user.username,password=current)
                        if user:
                                if new==confirm:
                                        user.set_password(new)
                                        user.save()
                                        messages.success(request,"password changed")
                                        logout(request)
                                        return redirect("log")
                                else:
                                        messages.error(request,"password mismatches!")
                                        return redirect("cp")
                        else:
                                messages.error(request,"password incorrect!")
                                return redirect("cp")
                else:
                        return render(request,"changepassword.html",{"form":form_data})        
                
class MyPostView(TemplateView):
        template_name="MyPost.html"
        def get_context_data(self, **kwargs):
                context=super().get_context_data(**kwargs)
                context["data"]=Posts.objects.filter(user=self.request.user).order_by('-datetime')
                return context
        
class EditBlogView(UpdateView):
        form_class=PostForm
        template_name="EditBlog.html"
        model=Posts
        success_url=reverse_lazy("mp")  
        pk_url_kwarg="pk"       
                     
class PostDeleteView(DeleteView):
        model=Posts
        template_name="deletepost.html"
        success_url=reverse_lazy("mp")
        
        
def addcomment(request,*args,**kwargs):
        if request.method=="POST":
                pid=kwargs.get("pid")
                post=Posts.objects.get(id=pid)
                user=request.user
                cmnt=request.POST.get("comments")
                Comments.objects.create(comments=cmnt,user=user,post=post)
                return redirect("uh")  
        
def addlike(request,*args,**kwargs):
        pid=kwargs.get("pid")
        post=Posts.objects.get(id=pid)
        user=request.user
        post.likes.add(user)
        post.save()
        return redirect("uh")             
        
        
                    

        
                             