from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    proj_type = models.CharField(max_length=128)
    # optionnel si c'est plus simple avec
    # author_user_id = models.ManyToManyField(to=settings.AUTH_USER_MODEL,
    #                                    on_delete=models.CASCADE)


class Contributor(models.Model):
    project_id = models.ForeignKey(to=Project,
                                   on_delete=models.CASCADE)
    # permissions =  choice field ?
    role = models.CharField(max_length=128)


class Issue(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=32)
    project_id = models.IntegerField()
    status = models.CharField(max_length=32)
    author_user_id = models.ManyToManyField(to=settings.AUTH_USER_MODEL)
    assignee_user_id = models.ManyToManyField(to=Project)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=1024)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
