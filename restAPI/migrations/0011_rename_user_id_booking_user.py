# Generated by Django 3.2.2 on 2021-05-10 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0010_auto_20210510_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='user_id',
            new_name='user',
        ),
    ]
