from django.contrib import admin
from .models import  Notes

# Register your models here.

admin.site.register(Notes)


class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Notes