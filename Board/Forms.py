from django import forms
from .models import Topics, Posts
class NewTopicForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea,max_length=4000)
    class  Meta:
        model = Topics
        fields = ['subject','message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Your message...'
            })
        }
