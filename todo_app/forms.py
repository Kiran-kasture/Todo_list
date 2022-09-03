from django import forms
from .models import Todo_list

class Todo_form(forms.ModelForm):
    class Meta:
        model=Todo_list
        fields=('title','description')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'})
        }
