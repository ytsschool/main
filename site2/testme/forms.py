#-*- encoding: utf-8 -*-
from django import forms
from testme.models import File, Bug


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args,  **kwargs)
        for f in self.fields.itervalues():
            css = f.widget.attrs.pop('class', '')
            if isinstance(f.widget, forms.FileInput):
                continue

            f.widget.attrs['class'] = css + ' form-control'


class FileUploadForm(BootstrapModelForm):
    class Meta:
        model = File


class ReportBugForm(BootstrapModelForm):
    class Meta:
        model = Bug