from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.CharField(null=False, blank=False,max_length=1000)
    email=models.EmailField(null=False, blank=False)
    content=models.TextField(null=False, blank=False)
    date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return self.name

  

