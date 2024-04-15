from django.db import models

# Create your models here.
class Service(models.Model):
    title =   models.CharField(("title"), max_length=50)
    description = models.CharField(("Description"), max_length=150)
    icon = models.CharField(("icon name"), max_length=50)
    