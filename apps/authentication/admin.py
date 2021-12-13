from django.contrib import admin
from django.contrib.auth.models import User
from apps.projects.models import Project
from apps.contributors.models import Contributor
from apps.issues.models import Issue
from apps.comments.models import Comment

class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    class Meta:
        model = User

admin.site.unregister(User)
admin.site.register(User, AdminUser)
admin.site.register(Comment)
admin.site.register(Issue)
admin.site.register(Contributor)
admin.site.register(Project)
