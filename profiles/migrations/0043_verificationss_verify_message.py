# Generated by Django 4.1.1 on 2022-12-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0042_rename_address_walkinprofiles_blk_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationss',
            name='verify_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
