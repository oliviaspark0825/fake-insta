from django.db import models
# setting 끝나면 models하기
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    img = models.ImageField(blank=True)# 빈값으로도 들어갈 수 있게
    
    
    def __str__(self):
        return self.content