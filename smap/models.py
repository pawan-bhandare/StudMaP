from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=112)
    email =models.EmailField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Note(models.Model):
    note_name=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=100,default="")
    dept=models.CharField(max_length=50,default="")
    clas=models.CharField(max_length=5,default="")
    sub=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="smap/images")
    
    def __str__(self):
        return self.note_name
    
    
class Paper(models.Model):
    paper_name=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=100,default="")
    dept=models.CharField(max_length=50,default="")
    clas=models.CharField(max_length=5,default="")
    sub=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="smap/images")
    
    def __str__(self):
        return self.paper_name
    