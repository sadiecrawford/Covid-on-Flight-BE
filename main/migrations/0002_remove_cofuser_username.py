# Generated by Django 3.1.2 on 2020-10-23 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cofuser',
            name='username',
        ),
    ]