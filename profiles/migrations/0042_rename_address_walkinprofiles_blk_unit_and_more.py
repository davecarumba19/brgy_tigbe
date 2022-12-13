# Generated by Django 4.1.1 on 2022-12-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0041_remove_profiles_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walkinprofiles',
            old_name='address',
            new_name='blk_unit',
        ),
        migrations.RemoveField(
            model_name='verificationss',
            name='address',
        ),
        migrations.AddField(
            model_name='walkinprofiles',
            name='phase_street',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]