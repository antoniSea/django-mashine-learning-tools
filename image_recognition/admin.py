from django.contrib import admin
from .models import Image

# add image model to admin panel
admin.site.register(Image)