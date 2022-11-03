from django.contrib import admin
from app.models import Author, JobPost, Location, Skill

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date')
    list_filter = ('date', 'salary')
    search_fields = ('date', 'salary', 'title', 'description' )
    fieldsets = (
        ('Basic Information', {
        'classes': ('collapse', 'wide'),   
        'fields':('title', 'description')
    }),
    ('More Information', {
        'classes': ('collapse', 'wide'),
        'fields': ('salary', 'slug')
    }),
    )
    # Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)