# Generated by Django 4.1.1 on 2022-12-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0051_remove_profiles_suffix_remove_walkinprofiles_suffix'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]
