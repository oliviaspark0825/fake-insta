from django import forms
from .models import Post, Image, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', ]
        # 여러개의 이미지를 올리고 싶으면
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="",)
    class Meta:
        model = Comment
        fields = ['content',]