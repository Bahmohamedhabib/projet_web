from django.shortcuts import render,redirect
from .forms import form_employe

def employer_list(request):
    return render(request,"Employer/employe_list.html")


def employer_form(request):
    if request.method =="POST":
        form=form_employe(request.POST).save('employe_list.html')
        

        
    form=form_employe
    return render(request,"Employer/employe_form.html",{'form':form})


def employer_delete(request):
    return

# Create your views here.
