# Generated by Django 4.0 on 2021-12-12 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoftDesk_API', '0011_remove_contributor_user_id_contributor_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoftDesk_API.project'),
        ),
    ]
