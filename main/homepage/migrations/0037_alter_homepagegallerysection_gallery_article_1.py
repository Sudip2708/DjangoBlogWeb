# Generated by Django 5.0 on 2024-04-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0036_rename_social_media_urls_footersettings_social_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagegallerysection',
            name='gallery_article_1',
            field=models.JSONField(default=dict),
        ),
    ]