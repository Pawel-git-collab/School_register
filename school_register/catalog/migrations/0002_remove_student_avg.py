# Generated by Django 3.2.21 on 2023-10-11 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='avg',
        ),
    ]