# Generated by Django 4.1.1 on 2022-11-25 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0031_alter_requests_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requests',
            options={'ordering': ['is_read', '-date_created']},
        ),
    ]
