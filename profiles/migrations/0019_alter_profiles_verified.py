# Generated by Django 4.1.1 on 2022-11-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_alter_profiles_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]