from django.urls import path
from accounts.views import*

urlpatterns = [
    path('r/',RegView.as_view(),name="reg"),
    path('l/',LogView.as_view(),name="log")
    
]
