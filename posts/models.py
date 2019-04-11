from django.db import models
# setting 끝나면 models하기
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    
    
    def __str__(self):
        return self.content