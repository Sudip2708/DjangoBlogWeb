# Generated by Django 5.0 on 2024-02-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_sidebar_user_author_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedBooleanField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='sidebar',
            field=models.BooleanField(default=True),
        ),
    ]