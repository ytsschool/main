from django import forms
from django.forms import ModelForm
from advert.models import board
from django.db import models

class addi(forms.ModelForm):

    class Meta:
        model = board
        fields = ('title', 'description','contact', 'money',)

    def save(self):
        obj = super(ItemDescForm, self).save(commit=False)
        return obj.save()
