from django import forms
from .models import *

class BioForm(forms.ModelForm): 
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.RadioSelect(attrs={}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "status":forms.TimeInput(attrs={"class":"form-control"}),
            
        }
        
class ChangePasswordForm(forms.Form): 
    c_password=forms.CharField(max_length=100,label="current password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    n_password=forms.CharField(max_length=100,label="new password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    conf_password=forms.CharField(max_length=100,label="confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))   
    
class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["image","caption"]  
        Widgets={
            "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control"})
        }  
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comments"]  
        Widgets={
            "comments":forms.Textarea(attrs={"class":"form-control"})
        }         