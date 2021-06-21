from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'header_image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'value': '', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'body': forms.Textarea(attrs={'class': 'form-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')