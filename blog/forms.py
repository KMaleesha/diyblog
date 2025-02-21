from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'rows': 8,
                    'cols': 50,
                    'id': 'description',
                    'placeholder': 'I dont think it helps to blame',
                }
            )
        }
        labels = {
            'comment_text': 'Description:'
        }