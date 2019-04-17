from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 유저와 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True)
    # 없으면 닉네임과 자기소개를 안받는데, 빈컬럼 생기면 오류가 뜨니까 처음에 빈값을 넣어주어야함
    introduction = models.TextField(blank=True)
    
    
    
    def __self__(self):
        return self.nickname

# user는 custom 한 뒤에 사용해야 함
class User(AbstractUser):
    # 저 사람이 나를팔로우하는 과정은 FOLLOWING
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name = 'followings')
    