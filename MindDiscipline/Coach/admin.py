from django.contrib import admin
from .models import Coach

# @admin.action()
# def 



class CoachCustomAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'first_name', 'patronymic_name', 'main_sport')
    list_display = ('last_name', 'first_name', 'patronymic_name', 'main_sport')
    list_display_links = ('last_name', 'first_name', 'patronymic_name')
    list_filter = ('main_sport', 'extra_sport', 'experience_years')
    filter_horizontal = ('practice',)


admin.site.register(Coach, CoachCustomAdmin)