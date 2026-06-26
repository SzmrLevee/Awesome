from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body':'Caption',
            'tags':'Category',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ...', 'class': 'font1 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url ...'}),
            'tags' : forms.CheckboxSelectMultiple(attrs={'class': 'peer sr-only'}),
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body':'',
            'tags' : 'Category',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'post-edit-textarea font1 text-4xl rounded-lg'}),
            'tags' : forms.CheckboxSelectMultiple(attrs={'class': 'peer sr-only'}),
        }
