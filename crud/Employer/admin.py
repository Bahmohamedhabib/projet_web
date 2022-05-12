from django.contrib import admin
from .models import Employer_enregister
from .models import Position



class afficher_employer(admin.ModelAdmin):
    list_display=('nom','emp_code','mobile','position')
    
admin.site.register(Position)  
admin.site.register(Employer_enregister,afficher_employer)


# Register your models here.
