from django import forms
from django.urls import reverse
from django.db import models
 
# creating a form
class InputForm(models.Model):
 
    document_name = models.CharField(max_length = 200)
    value = models.IntegerField(
        help_text = "€"
        )

    def get_absolute_url(self):
        return reverse('forms:home')