# Generated by Django 3.2.2 on 2021-05-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('photo_url', models.URLField()),
            ],
        ),
    ]