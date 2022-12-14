# Generated by Django 4.1.1 on 2022-10-09 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_remove_requests_owner_requests_is_read_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reports',
            options={'ordering': ['is_read', '-date_created']},
        ),
        migrations.AlterModelOptions(
            name='requests',
            options={'ordering': ['is_read', '-date_created']},
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='owner',
            new_name='sender',
        ),
        migrations.AddField(
            model_name='reports',
            name='is_read',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='reports',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report', to='profiles.profiles'),
        ),
        migrations.AddField(
            model_name='requests',
            name='purpose',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
