# Generated by Django 4.0 on 2021-12-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoftDesk_API', '0008_alter_issue_assignee_user_id_alter_issue_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'author'), ('CONTRIBUTOR', 'contributor')], max_length=16),
        ),
    ]