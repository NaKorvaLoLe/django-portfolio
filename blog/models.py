from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images', blank=True)
    url = models.URLField(blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title