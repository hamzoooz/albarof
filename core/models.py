from django.db import models

# Create your models here, null=True, blank=True.
class Service(models.Model):
    title =   models.CharField(("title"), max_length=50, null=True, blank=True)
    description = models.CharField(("Description"), max_length=150, null=True, blank=True)
    icon = models.CharField(("icon name"), max_length=50, null=True, blank=True)
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name  = models.CharField(max_length = 150, null=True, blank=True)
    def __str__(self):
        return self.name
     
class Events(models.Model):
    title = models.CharField(max_length = 150, null=True, blank=True)
    image = models.ImageField(upload_to='Events', height_field=None, width_field=None, max_length=100, null=True, blank=True)
    description = models.CharField(max_length = 150, null=True, blank=True)
    link = models.URLField(max_length = 200, null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name= (""), on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    