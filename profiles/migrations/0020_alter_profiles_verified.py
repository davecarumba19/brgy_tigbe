# Generated by Django 4.1.1 on 2022-11-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_alter_profiles_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='verified',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=500, null=True),
        ),
    ]
