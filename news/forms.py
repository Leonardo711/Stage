from django import forms
from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model =  News
        fields = ('title', 'content')
        widgets = {
            "title": forms.TextInput,
           "content":forms.Textarea,
        }