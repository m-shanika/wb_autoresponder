# Generated by Django 5.1.4 on 2024-12-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoresponder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='token',
        ),
        migrations.AddField(
            model_name='organization',
            name='official_token',
            field=models.CharField(default=1, max_length=255, verbose_name='Токен для API'),
            preserve_default=False,
        ),
    ]
