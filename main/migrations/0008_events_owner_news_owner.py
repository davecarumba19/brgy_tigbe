# Generated by Django 4.1.1 on 2022-10-18 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_messages_your_file'),
        ('main', '0007_skofficials_rename_officials_brgyofficials'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profiles'),
        ),
        migrations.AddField(
            model_name='news',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profiles'),
        ),
    ]