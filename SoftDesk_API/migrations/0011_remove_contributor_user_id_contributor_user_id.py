# Generated by Django 4.0 on 2021-12-12 22:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SoftDesk_API', '0010_remove_project_author_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contributor',
            name='user_id',
            field=models.ManyToManyField(related_name='contributor', to=settings.AUTH_USER_MODEL),
        ),
    ]