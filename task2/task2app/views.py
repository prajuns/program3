from django.shortcuts import render
from . models import Data
from . models import Person
# Create your views here.
def demo(request):
    obj=Data.objects.all()
    obj2 = Person.objects.all()
    return render(request,'index.html',{'result':obj,'result2':obj2})
