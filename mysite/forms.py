from django import forms
from mysite.models import File

class FileForm(forms.Form):
    file_name = forms.CharField(label='File name', max_length=100)
    parent = forms.ModelChoiceField(queryset=File.objects.all())