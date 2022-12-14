# Generated by Django 4.1.1 on 2022-12-04 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0033_reports_hide'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtendModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=500, null=True)),
                ('vaccine', models.CharField(blank=True, choices=[('Vaccinated', 'Vaccinated'), ('Not Vaccinated', 'Not Vaccinated')], max_length=500, null=True)),
                ('profile_image', models.ImageField(blank=True, default='default profile.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
