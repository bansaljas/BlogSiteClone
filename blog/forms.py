from django import forms
from .models import Post,Comment

# In this we will use customized widgets
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','author','text')

        widgets={
            'title': forms.TextInput(attrbs={'class': 'textinputclass'}),
            'text': forms.TextArea(attrbs={'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('author','text')
        
        widgets={
            'author': forms.TextInput(attrbs={'class': 'textinputclass'}),
            'text': forms.TextArea(attrbs={'class': 'editable medium-editor-textarea postcontent'})
        }
