# Generated by Django 5.0 on 2024-02-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_customuser_sidebar_category_navigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sidebar_search_options',
            field=models.BooleanField(default=False),
        ),
    ]