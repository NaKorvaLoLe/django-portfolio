from django.db import models

# Create your models here.
class Html_CSS(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url_site = models.URLField(blank=True)
    url_repos = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    
    
class React_JS(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/projects')
    url_site = models.URLField(blank=False)
    url_repos = models.URLField(blank=False)
    
    def __str__(self):
        return self.title    
    
    
class Stack(models.Model):
    image = models.FileField(upload_to="portfolio/images/stack")
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title 
    
