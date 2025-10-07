from django import forms
from .models import Post
from .models import Comment
# ModelForm for Post creation and updating
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        } 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'})
        }