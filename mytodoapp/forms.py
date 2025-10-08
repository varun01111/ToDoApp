from django import forms
from .models import ToDO


class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDO
        fields=("title","des")

