from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# setting 끝나면 models하기
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    # img = models.ImageField(blank=True)# 빈값으로도 들어갈 수 있게
    
 
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