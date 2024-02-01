# Generated by Django 5.0 on 2024-02-01 12:46

import articles.models.article_category
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=articles.models.article_category.ArticleCategory.get_default_category_id, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='article_category', to='articles.articlecategory'),
        ),
    ]
