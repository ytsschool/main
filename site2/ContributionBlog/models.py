#coding=utf-8
from django.db import models
import datetime
class User(models.Model):
    name = models.CharField(max_length=256)
class Project(models.Model):
    name = models.CharField(max_length=256)
    project_auth = models.CharField(max_length=256,blank=False)
class CommitInfo(models.Model):
    user = models.ForeignKey(User)
    commitDate = models.DateTimeField(default=datetime.datetime.now)
    revision = models.IntegerField(blank=False)
    project = models.ForeignKey(Project)
    commitMessage = models.TextField(default='')
    filesChanged = models.IntegerField(default=0)
    linesModified = models.IntegerField(default=0)
    linesAdded = models.IntegerField(default=0)
    linesRemoved = models.IntegerField(default=0)
    class Meta:
        unique_together=(('project','revision'))
# Create your models here.
