from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
# setting 끝나면 models하기
# Create your models here.

# 처음에 안만들면 나중에 참조를 못하니까
class Hashtag(models.Model):
    content = models.TextField(unique=True)
    
    def __str__(self):
        return self.content


class Post(models.Model):
    # img = models.ImageField(blank=True)# 빈값으로도 들어갈 수 있게
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    
    
    def __str__(self):
        return self.content
        
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content        
        
        
        

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 삭제되면 딸려있던 이미지도 삭제될 수 있도록
    file = ProcessedImageField(
                upload_to='posts/images',							# 저장 위치
                processors=[ResizeToFill(600, 600)],		# 처리할 작업 목록
                format='JPEG',													# 저장 포맷
                options={'quality': 90},								# 옵션
    				)
