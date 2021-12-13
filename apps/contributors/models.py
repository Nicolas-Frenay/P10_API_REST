from django.db import models
from django.conf import settings
from apps.projects.models import Project

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
