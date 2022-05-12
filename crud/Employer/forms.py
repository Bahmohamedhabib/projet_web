
from dataclasses import field, fields
from django import forms
from .models import Employer_enregister



class form_employe(forms.ModelForm):
    class Meta:
        model=Employer_enregister
        fields='__all__'
    
    # def __init__(self, *args, **kwargs):
    #     super(Employer_enregister,self).__init__(*args, **kwargs)
    #     self.files['position'].empty_label ="select"
        