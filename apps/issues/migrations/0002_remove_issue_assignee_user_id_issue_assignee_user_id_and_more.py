# Generated by Django 4.0 on 2021-12-14 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='assignee_user_id',
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='auth.user'),
        ),
        migrations.RemoveField(
            model_name='issue',
            name='author_user_id',
        ),
        migrations.AddField(
            model_name='issue',
            name='author_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='auth.user'),
        ),
    ]
