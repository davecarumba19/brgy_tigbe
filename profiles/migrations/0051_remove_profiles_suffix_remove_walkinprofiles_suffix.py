# Generated by Django 4.1.1 on 2022-12-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0050_profiles_suffix_walkinprofiles_suffix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='suffix',
        ),
        migrations.RemoveField(
            model_name='walkinprofiles',
            name='suffix',
        ),
    ]