# Generated by Django 4.1.1 on 2022-09-21 03:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profiles_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
