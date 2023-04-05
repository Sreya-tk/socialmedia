from django.urls import path
from user.views import*

urlpatterns = [
     path('home/',UserHome.as_view(),name="uh"),
     path('profile/',ProfileView.as_view(),name="pro"),
     path('bio/',BioView.as_view(),name="bio"),
     path('ebio/<int:pk>/',EditBioView.as_view(),name="ebio"),
     path('cp/',ChangePasswordView.as_view(),name="cp"),
     path('mp/',MyPostView.as_view(),name="mp"),
     path('eblog/<int:pk>/',EditBlogView.as_view(),name="eblog"),
     path('pdelete/<int:pk>/',PostDeleteView.as_view(),name="pdelete"),
     path('addcmnt/<int:pid>/',addcomment,name="addc"),
     path('addlike/<int:pid>/',addlike,name="addl")
     
    
]
