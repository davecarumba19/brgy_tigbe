# Generated by Django 4.1.1 on 2022-11-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_alter_profiles_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='username',
            field=models.CharField(blank=True, editable=False, max_length=1000, null=True),
        ),
    ]
