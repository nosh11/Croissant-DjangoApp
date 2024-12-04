from django.db import models

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    letter_body = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

    
