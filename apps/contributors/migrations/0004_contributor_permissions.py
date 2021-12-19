# Generated by Django 4.0 on 2021-12-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0003_alter_contributor_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='permissions',
            field=models.CharField(choices=[('AUTHOR', 'author'), ('CONTRIBUTOR', 'contributor')], default='CONTRIBUTOR', max_length=16),
        ),
    ]
