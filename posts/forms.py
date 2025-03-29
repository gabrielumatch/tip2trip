from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'location']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Share your journey...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Add location...'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 text-sm',
                'placeholder': 'Write a comment...'
            })
        } 