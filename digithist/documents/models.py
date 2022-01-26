from django.db import models

class Document(models.Model):

    path = models.fields.CharField(max_length=100)
    
    class Type(models.TextChoices):
        TYPE_1 = '1'
        TYPE_2 = '2'
        TYPE_3 = '3'

    type = models.fields.CharField(choices=Type.choices, max_length=5)
    description = models.fields.CharField(max_length=1000)
    value = models.fields.IntegerField()
    done = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.path}'