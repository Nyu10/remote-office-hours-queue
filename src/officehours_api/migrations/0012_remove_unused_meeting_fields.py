# Generated by Django 3.0.5 on 2020-04-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officehours_api', '0011_add_queue_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='started_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='ended_at',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='removed_at',
        ),
    ]
