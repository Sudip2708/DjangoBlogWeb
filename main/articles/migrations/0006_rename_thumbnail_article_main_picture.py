# Generated by Django 5.0 on 2024-01-17 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_main_picture_high_article_main_picture_low_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumbnail',
            new_name='main_picture',
        ),
    ]