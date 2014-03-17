from django.contrib import admin
from main.models import App

class AppAdmin(admin.ModelAdmin):
    list_display = ('name','link')

admin.site.register(App, AppAdmin)