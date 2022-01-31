from django import forms
from documents.models import Document, Folder

class DocumentForm(forms.ModelForm):
   class Meta:
     model = Document
     fields = '__all__'
     #exclude = ('active', 'official_homepage') 

class FolderForm(forms.ModelForm):
   class Meta:
     model = Folder
     fields = '__all__'