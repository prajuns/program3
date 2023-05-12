from django.contrib import admin
from .models import Data
from . models import Person

# Register your models here.
admin.site.register(Data)
admin.site.register(Person)
