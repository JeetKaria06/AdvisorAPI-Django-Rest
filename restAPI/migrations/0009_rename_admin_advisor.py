# Generated by Django 3.2.2 on 2021-05-10 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0008_alter_user_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Advisor',
        ),
    ]