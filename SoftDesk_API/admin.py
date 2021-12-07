from django.contrib import admin
from SoftDesk_API.models import Project, Issue, Contributor, Comment

# class ProjectAdmin(admin.ModelAdmin):



admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Contributor)
admin.site.register(Comment)
