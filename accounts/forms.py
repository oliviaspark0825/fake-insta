from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
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
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # Meta class도 상속받을 수 있다.
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        