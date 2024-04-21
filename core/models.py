from django.db import models

from dynamic_models.models import AbstractModelSchema


# Create your models here, null=True, blank=True.
class Service(models.Model):
    title =   models.CharField(("title"), max_length=50, null=True, blank=True)
    description = models.CharField(("Description"), max_length=150, null=True, blank=True)
    # image = models.ImageField(_(""), upload_to="None", height_field=None, width_field=None, max_length=None)
    icon = models.CharField(("icon name"), max_length=50, null=True, blank=True)
    def __str__(self):
        return self.title

class SubServers(models.Model):
    Service = models.ForeignKey(Service ,  on_delete=models.CASCADE ,null=True, blank=True )
    image1 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image2 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image3 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image4 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image5 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image6 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image7 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image8 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image9 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image10 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image11 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image12 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image13 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image14 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image15 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image16 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image17 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image18 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image19 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image20 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image21 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image22 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image23 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image24 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image25 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image26 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image27 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image28 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image29 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image30 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image31 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image32 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image33 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image34 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image35 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image36 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image37 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image38 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image39 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    image40 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    
    
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
    

class DynamicModel(AbstractModelSchema):
    pass

class DynamicField(models.Model):
    Service = models.ForeignKey(Service ,  on_delete=models.CASCADE ,null=True, blank=True )
    image1 = models.ImageField(upload_to="SubServers",null=True, blank=True ) 
    model = models.ForeignKey(DynamicModel, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)
