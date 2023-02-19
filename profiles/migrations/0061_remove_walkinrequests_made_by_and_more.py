# Generated by Django 4.1.1 on 2022-12-15 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0060_rename_made_by_requests_sender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walkinrequests',
            name='made_by',
        ),
        migrations.RemoveField(
            model_name='walkinrequests',
            name='owner_name',
        ),
        migrations.AddField(
            model_name='walkinrequests',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.walkinprofiles'),
        ),
    ]