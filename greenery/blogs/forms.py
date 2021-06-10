from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': choices}),
        'author': forms.Select(attrs={'class': 'form-input'}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-input'}),
        'body': forms.Textarea(attrs={'class': 'form-input'}),
        
    }