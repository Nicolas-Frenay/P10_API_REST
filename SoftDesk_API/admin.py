
from django.contrib import admin
from SoftDesk_API.models import Project, Issue, Contributor, Comment
from django.contrib.auth.models import User

class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    class Meta:
        model = User




admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Contributor)
admin.site.register(Comment)
admin.site.unregister(User)
admin.site.register(User, AdminUser)