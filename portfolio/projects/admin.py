from django.contrib import admin

from .models import Project

admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin Area'
admin.site.index_title = 'Welcome to the Portfolio Admin Area'

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['title', 'description', 'technology']}),
                 ('Date Information', {'fields':['pub_date'], 'classes':
                 ['collapse']}), ]

admin.site.register(Project, ProjectAdmin)
