from django.contrib import admin
from .models import Profile


# register profile and Note model to admin
admin.site.register(Profile)