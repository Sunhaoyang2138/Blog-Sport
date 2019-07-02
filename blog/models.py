from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField(blank=True, null=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    image=models.ImageField(upload_to='sports',blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    sport=models.CharField(max_length=200,blank=True,null=True)
    duration=models.DurationField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

