from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'introduction', 'user_id',]
admin.site.register(Profile, ProfileAdmin)


#만들필요 없으니까, 내가 만든 유저를 상속받아서 
admin.site.register(User,UserAdmin)