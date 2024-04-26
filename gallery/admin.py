# gallery/admin.py
from django.contrib import admin
from .models import Artist, Artwork
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Artist)
admin.site.register(Artwork)
