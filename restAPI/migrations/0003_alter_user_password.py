# Generated by Django 3.2.2 on 2021-05-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]