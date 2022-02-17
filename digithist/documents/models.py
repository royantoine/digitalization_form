from django.db import models

class Document(models.Model):

    path = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=100)
    
    #path2 = models.fields.FilePathField(allow_files=False, allow_folders=True)    
    class Type(models.TextChoices):
        TYPE_1 = '1'
        TYPE_2 = '2'
        TYPE_3 = '3'

    type = models.fields.CharField(choices=Type.choices, max_length=5, default='1')
    description = models.fields.CharField(max_length=1000, default="")
    value = models.fields.IntegerField(default=0)
    done = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.path}'

class Folder(models.Model):

    path = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=100)

    def __str__(self):
        return f'{self.path}'

class Sale(models.Model):

    name = models.fields.CharField(default="", max_length=100)
    value =models.fields.IntegerField(default=0)
    path = models.ForeignKey(Document, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'