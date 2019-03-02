from django.contrib import admin
from .models import  Notes,Labels, MapLabel


# Register your models here.
admin.site.register(Notes)
admin.site.register(Labels)
admin.site.register(MapLabel)

class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Notes