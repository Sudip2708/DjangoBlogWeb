# Generated by Django 5.0.4 on 2024-05-09 09:05

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_footer_section', models.BooleanField(default=True, verbose_name='Display Footer Section')),
                ('address_values', models.JSONField(default=dict)),
                ('social_media', models.JSONField(default=dict)),
                ('site_links', models.JSONField(default=dict)),
                ('articles', models.JSONField(default=dict)),
                ('end_line', models.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageDividerSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_divider_section', models.BooleanField(default=True, verbose_name='Display Divider Section')),
                ('divider_image', models.ImageField(blank=True, default='images/homepage/default/divider-bg.jpg', null=True, upload_to='images/homepage/', verbose_name='Divider Section Image')),
                ('divider_text', tinymce.models.HTMLField(blank=True, default='<h2>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</h2>', null=True, verbose_name='Divider Section Text')),
                ('divider_link_title', models.CharField(blank=True, default='View More', max_length=100, null=True, verbose_name='Divider Section Link Title')),
                ('divider_link', models.URLField(blank=True, default='#!', null=True, verbose_name='Divider Section Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageGallerySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_gallery_section', models.BooleanField(default=True, verbose_name='Display Gallery Section')),
                ('gallery_article_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_article_1', to='articles.article', verbose_name='Gallery Article 1')),
                ('gallery_article_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_article_2', to='articles.article', verbose_name='Gallery Article 2')),
                ('gallery_article_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_article_3', to='articles.article', verbose_name='Gallery Article 3')),
                ('gallery_article_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_article_4', to='articles.article', verbose_name='Gallery Article 4')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageHeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_hero_section', models.BooleanField(default=True, verbose_name='Display Hero Section')),
                ('hero_image', models.ImageField(blank=True, default='images/homepage/default/hero.jpg', null=True, upload_to='images/homepage/', verbose_name='Hero Section Image')),
                ('hero_title', tinymce.models.HTMLField(blank=True, default='<h1>Bootstrap 5 Blog - A free template by Bootstrapious</h1>', null=True, verbose_name='Hero Section Title')),
                ('hero_link_title', models.CharField(blank=True, default='Discover More', max_length=100, null=True, verbose_name='Hero Section Link Title')),
                ('hero_link', models.URLField(blank=True, default='#!', null=True, verbose_name='Hero Section Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageIntroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_intro_section', models.BooleanField(default=True, verbose_name='Display Intro Section')),
                ('intro_title', tinymce.models.HTMLField(blank=True, default="<div><span style='font-size: 28px;'><strong>Some great intro here</strong></span></div>", null=True, verbose_name='Intro Section Title')),
                ('intro_description', tinymce.models.HTMLField(blank=True, default="<div style='line-height: 2;'><span style='font-size: 16.5pt; color: rgb(0, 0, 0);'><span style='color: rgb(33, 33, 33);'>Place a nice&nbsp;</span><strong>introduction</strong><span style='color: rgb(33, 33, 33);'>&nbsp;here</span>&nbsp;<strong>to catch reader's attention</strong>. <span style='color: rgb(33, 33, 33);'>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderi.</span></span></div>", null=True, verbose_name='Intro Section Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageFeaturedArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_featured_section', models.BooleanField(default=True, verbose_name='Display Featured Section')),
                ('featured_article_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_article_1', to='articles.article', verbose_name='Featured Article 1')),
                ('featured_article_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_article_2', to='articles.article', verbose_name='Featured Article 2')),
                ('featured_article_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_article_3', to='articles.article', verbose_name='Featured Article 3')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageLatestArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_latest_section', models.BooleanField(default=True, verbose_name='Display Latest Section')),
                ('latest_title', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Latest Articles Title')),
                ('latest_description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Latest Articles Description')),
                ('latest_article_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_article_1', to='articles.article', verbose_name='Latest Article 1')),
                ('latest_article_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_article_2', to='articles.article', verbose_name='Latest Article 2')),
                ('latest_article_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_article_3', to='articles.article', verbose_name='Latest Article 3')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('subscribed_at', models.DateTimeField(auto_now_add=True, verbose_name='Subscription Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Subscribed User', related_name='newsletter_subscriptions')),
            ],
            options={
                'verbose_name': 'Newsletter Subscriber',
                'verbose_name_plural': 'Newsletter Subscribers',
            },
        ),
        migrations.CreateModel(
            name='HomePageNewsletterSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_newsletter_section', models.BooleanField(default=True, verbose_name='Display Newsletter Section')),
                ('newsletter_title', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Newsletter Section Title')),
                ('newsletter_description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Newsletter Section Description')),
                ('newsletter_subscribers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_page_subscribers', to='homepage.newslettersubscriber', verbose_name='Newsletter Subscribers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
