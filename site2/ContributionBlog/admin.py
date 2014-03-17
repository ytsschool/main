#coding=utf-8
from django.contrib import admin

from ContributionBlog.models import CommitInfo,User,Project
class UserAdmin(admin.ModelAdmin):
    fields = ['name']
class ProjectAdmin(admin.ModelAdmin):
    fields = ['name','project_auth']

class CommitInfoAdmin(admin.ModelAdmin):
    fields = ['project','user','commitDate','revision']
# Register your models here.
admin.site.register(CommitInfo,CommitInfoAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Project,ProjectAdmin)

