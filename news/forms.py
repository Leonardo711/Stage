from django import forms
from news.models import News
from ckeditor.widgets import CKEditorWidget


class NewsForm(forms.ModelForm):
    class Meta:
        model =  News
        fields = ('title', 'content')
        widgets = {
            "title": forms.TextInput,
           "content":CKEditorWidget,
        }