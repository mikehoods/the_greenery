from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            # 'author': forms.Select(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'value': '', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'body': forms.Textarea(attrs={'class': 'form-input'}),
        }