from django import forms
from .models import Post

# ModelForm for Post creation and updating
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  
