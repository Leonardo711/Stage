from django import forms
from team.models import Member



class MemberForm(forms.ModelForm):
    class Meta:
        model =  Member
        fields = ('name', 'teamName', 'priority', 'profile')
        widgets = {'name': forms.TextInput(),
                   "teamName":forms.TextInput(),
                   'profile':forms.Textarea()}
