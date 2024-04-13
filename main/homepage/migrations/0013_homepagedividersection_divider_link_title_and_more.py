# Generated by Django 5.0 on 2024-04-05 11:37

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_alter_homepageherosection_hero_link_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagedividersection',
            name='divider_link_title',
            field=models.CharField(blank=True, default='VIEW MORE', max_length=100, null=True, verbose_name='Hero Section Link Title'),
        ),
        migrations.AlterField(
            model_name='homepagedividersection',
            name='divider_text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Divider Section Text'),
        ),
        migrations.AlterField(
            model_name='homepageherosection',
            name='hero_title',
            field=tinymce.models.HTMLField(blank=True, default='<h1>Bootstrap 5 Blog - A free template by Bootstrapious</h1>', null=True, verbose_name='Hero Section Title'),
        ),
    ]