from django.db import models
from django.conf import settings


class Project(models.Model):
    BACK_END = 'BACK_END'
    FRONT_END = 'FRONT_END'
    IOS = 'IOS'
    ANDROID = 'ANDROID'

    PROJECT_TYPE = (
        (BACK_END, 'back_end'),
        (FRONT_END, 'front_end'),
        (IOS, 'ios'),
        (ANDROID, 'android')
    )

    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=1024, null=False)
    proj_type = models.CharField(max_length=16, choices=PROJECT_TYPE,
                                 verbose_name='project_type', null=False)


class Contributor(models.Model):
    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    ROLE_LIST = (
        (AUTHOR, 'author'),
        (CONTRIBUTOR, 'contributor')
    )
    user_id = models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                            related_name='contributor')
    project_id = models.ForeignKey(to=Project,
                                   on_delete=models.CASCADE)
    # permissions =  choice field ?
    role = models.CharField(max_length=16, choices=ROLE_LIST)


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
    project_id = models.IntegerField()
    status = models.CharField(max_length=16, choices=STATUS_LIST)
    author_user_id = models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                            related_name='author')
    assignee_user_id = models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                              related_name='assignee',
                                              default=author_user_id)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=1024)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
