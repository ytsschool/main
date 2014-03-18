#-*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
import os


class File(models.Model):
    file = models.FileField(u'Файл', upload_to=settings.UPLOAD_DIR)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        return os.path.basename(self.file.name)

    def __unicode__(self):
        return self.name


class Bug(models.Model):
    name = models.CharField(u'Название', max_length=500)
    description = models.TextField(u'Описание')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name