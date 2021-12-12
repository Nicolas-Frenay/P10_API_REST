# Generated by Django 4.0 on 2021-12-11 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('SoftDesk_API', '0005_project_author_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author_user_id',
        ),
        migrations.AddField(
            model_name='project',
            name='author_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
