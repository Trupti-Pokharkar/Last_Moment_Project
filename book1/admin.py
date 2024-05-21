from django.contrib import admin
from .models import Course, Publication
# Register your models here.
class PublicationInline(admin.TabularInline):
    model = Publication

class CourseAdmin(admin.ModelAdmin):
    inlines = [PublicationInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Publication)

