# Generated by Django 4.1.1 on 2022-12-15 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0061_remove_walkinrequests_made_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walkinrequests',
            name='owner',
        ),
    ]
