# Generated by Django 4.1.1 on 2022-11-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_alter_messages_receiver_alter_messages_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='vaccine',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=500, null=True),
        ),
    ]
