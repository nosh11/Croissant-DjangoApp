from django.db import models

# Create your models here.
class PortFolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/', default='static/portfolio/images/logo.jpg')
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']