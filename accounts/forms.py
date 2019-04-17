from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile
from django import forms
#회원수정 폼
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', ]
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'introduction',]