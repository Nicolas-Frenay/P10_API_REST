from django.contrib import admin
from SoftDesk_API.models import Project, Issue, Contributor, Comment
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password']



admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Contributor)
admin.site.register(Comment)
