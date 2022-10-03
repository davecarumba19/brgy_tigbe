# Generated by Django 4.1.1 on 2022-09-14 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='news',
            old_name='where',
            new_name='location',
        ),
    ]
