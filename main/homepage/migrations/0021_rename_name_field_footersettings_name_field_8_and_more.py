# Generated by Django 5.0 on 2024-04-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_footersettings_footer_article_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footersettings',
            old_name='name_field',
            new_name='name_field_8',
        ),
        migrations.RenameField(
            model_name='footersettings',
            old_name='url_field',
            new_name='url_field8',
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 1 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 2 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 3 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 4 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 5 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_6',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 6 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='name_field_7',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Site Link 7 Name'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field1',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 1 URL'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field2',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 2 URL'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field3',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 3 URL'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field4',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 4 URL'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field5',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 5 URL'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field6',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 6 URL'),
        ),
        migrations.AddField(
            model_name='footersettings',
            name='url_field7',
            field=models.URLField(blank=True, null=True, verbose_name='Site Link 7 URL'),
        ),
    ]
