from django.db import models
from django.conf import settings
from apps.projects.models import Project


class Issue(models.Model):
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    PRIORITY_LIST = (
        (HIGH, 'high'),
        (MEDIUM, 'medium'),
        (LOW, 'low')
    )

    BUG = 'BUG'
    IMPROVEMENT = 'IMPROVEMENT'
    TASK = 'TASK'

    TAGS_LIST = (
        (BUG, 'bug'),
        (IMPROVEMENT, 'improvement'),
        (TASK, 'task')
    )

    TO_DO = 'TO_DO'
    ONGOING = 'ONGOING'
    FINISH = 'FINISH'

    STATUS_LIST = (
        (TO_DO, 'to_do'),
        (ONGOING, 'ongoing'),
        (FINISH, 'finish')
    )

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=1024)
    tag = models.CharField(max_length=16, choices=TAGS_LIST)
    priority = models.CharField(max_length=16, choices=PRIORITY_LIST)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUS_LIST)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       null=True,
                                       on_delete=models.CASCADE,
                                       related_name='author')
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                         null=True,
                                         on_delete=models.CASCADE,
                                         related_name='assignee')
    created_time = models.DateTimeField(auto_now_add=True)

