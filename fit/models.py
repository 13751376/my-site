from django.db import models

# Create your models here.
class Topic(models.Model): 
    title=models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class User(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField() 
    time=models.DateTimeField()   
