from . import views
from django.urls import path




urlpatterns = [    
    path('Homepage/', views.Homepage),
    path('Index/', views.Index),
    ]
