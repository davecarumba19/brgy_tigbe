# Generated by Django 4.1.1 on 2022-12-15 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0054_alter_reports_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='sender',
        ),
    ]