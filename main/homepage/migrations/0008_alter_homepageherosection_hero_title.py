# Generated by Django 5.0 on 2024-04-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_homepageherosection_hero_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageherosection',
            name='hero_title',
            field=models.CharField(blank=True, default='Bootstrap 5 Blog - A free template by Bootstrapious', max_length=100, null=True, verbose_name='Hero Section Title'),
        ),
    ]