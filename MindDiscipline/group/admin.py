from django.contrib import admin
from .models import Group


class CustomGroupAdmin(admin.ModelAdmin):
    search_fields = ('sport',)

admin.site.register(Group, CustomGroupAdmin)