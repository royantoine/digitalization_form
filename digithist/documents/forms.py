from django import forms
from documents.models import Document, Folder, Sale
from django.forms.models import inlineformset_factory

class DocumentForm(forms.ModelForm):
   class Meta:
     model = Document
     fields = '__all__'
     #exclude = ('active', 'official_homepage') 

class FolderForm(forms.ModelForm):
   class Meta:
     model = Folder
     fields = '__all__'

class SaleForm(forms.ModelForm):
   class Meta:
     model = Sale
     fields = '__all__'

SaleFormset = inlineformset_factory(
    Document, 
    Sale, 
    form=SaleForm,
    extra=5
    #fields=('name',)
)
