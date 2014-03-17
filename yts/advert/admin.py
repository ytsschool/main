from django.contrib import admin
from advert.models import board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title','description','contact']
    list_display = ('title', 'pub_date')
admin.site.register(board, BoardAdmin)


