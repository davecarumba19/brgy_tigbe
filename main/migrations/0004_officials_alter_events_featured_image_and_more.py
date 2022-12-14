# Generated by Django 4.1.1 on 2022-09-14 14:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_events_rename_where_news_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officials',
            fields=[
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('position', models.CharField(blank=True, max_length=1000, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
