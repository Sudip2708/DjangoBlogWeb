# Generated by Django 5.0 on 2024-02-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_sidebar_user_user_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sidebar_user_author_menu',
            field=models.BooleanField(default=False),
        ),
    ]
