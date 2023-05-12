from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Person(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='photo')
    desc=models.TextField()


    def __str__(self):
        return self.name
