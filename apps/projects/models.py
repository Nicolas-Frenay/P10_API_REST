from django.db import models


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
