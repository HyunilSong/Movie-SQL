from django import forms
from django.contrib import admin

from .models import *

# Register your models here.

# User admin
admin.site.register(CustomerUser),

# Movie admin
admin.site.register(Movie_info),
admin.site.register(Screen_info),
admin.site.register(Screen),
admin.site.register(Customer_Pesonal_info),
admin.site.register(Reservation),
admin.site.register(Employer_Personal_info),
