# Generated by Django 4.1.1 on 2022-12-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0038_remove_walkinprofiles_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='your_file',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='your_message',
        ),
        migrations.AddField(
            model_name='messages',
            name='document_type',
            field=models.CharField(blank=True, choices=[('Brgy. Clearance', 'Brgy. Clearance'), ('Certificate of Ingency', 'Certificate of Ingency')], max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='purpose',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
