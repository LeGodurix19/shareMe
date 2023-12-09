from django.contrib import admin
from .models import CustomUser, Link, LinkUser

admin.site.register(CustomUser)
admin.site.register(Link)
admin.site.register(LinkUser)