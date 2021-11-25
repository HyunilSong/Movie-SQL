from django.contrib import admin

# Register your models here.

from .models import Movie_info
from .models import Screen_info
from .models import Screen
from .models import Customer_Pesonal_info
from .models import Reservation
from .models import Employer_Personal_info

admin.site.register(Movie_info)
admin.site.register(Screen_info)
admin.site.register(Screen)
admin.site.register(Customer_Pesonal_info)
admin.site.register(Reservation)
admin.site.register(Employer_Personal_info)