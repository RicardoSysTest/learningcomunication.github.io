from django.contrib import admin

from . import models

# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register Notes Model
admin.site.register(models.Task, NotesAdmin)
