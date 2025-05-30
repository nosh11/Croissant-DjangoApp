from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = ColorField(default='#533fab', format='hex')

    def __str__(self):
        return self.name

class PortFolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/', blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']