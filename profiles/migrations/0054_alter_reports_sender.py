# Generated by Django 4.1.1 on 2022-12-15 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0053_alter_reports_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profiles'),
        ),
    ]