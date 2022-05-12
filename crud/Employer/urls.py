from django.urls import path,include
from .import views


urlpatterns = [
    
    path('list/',views.employer_list,name='employer_list'),
    path('',views.employer_form,name='employer_form')
]
