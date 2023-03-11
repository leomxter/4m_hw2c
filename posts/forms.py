from django import forms
from posts.models import Comment, PostCreate


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "text")

class PostForm(forms.ModelForm):
    class Meta:
        model = PostCreate
        fields = ("title", "content")