from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    sportart=models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    duration=models.CharField(max_length=100,blank=True,null=True)
    length=models.IntegerField(blank=True, null=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    text=models.TextField(blank=True, null=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

