# Generated by Django 4.1.5 on 2023-01-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
