from django import forms
from django.db import models
from django.db.models import fields
from django.forms.widgets import Widget
from settings.models import infoform


class catagories(forms.ModelForm):
    name = models.CharField(max_length=50,Widget=forms.Textarea(attrs={'class':'form-control'}))


    class meta:
        model = infoform
        fields = '__all__'