# Generated by Django 5.0 on 2024-04-08 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0029_footersettings_footer_end_left_link_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footersettings',
            old_name='footer_end_left_link_text',
            new_name='end_left_link_text',
        ),
        migrations.RenameField(
            model_name='footersettings',
            old_name='future_end_left_link_url',
            new_name='end_left_link_url',
        ),
        migrations.RenameField(
            model_name='footersettings',
            old_name='footer_end_left_text',
            new_name='end_left_text',
        ),
        migrations.RenameField(
            model_name='footersettings',
            old_name='future_end_right_link_url',
            new_name='end_right_link_url',
        ),
        migrations.RenameField(
            model_name='footersettings',
            old_name='footer_end_right_text',
            new_name='end_right_text',
        ),
    ]
