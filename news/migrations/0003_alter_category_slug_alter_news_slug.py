# Generated by Django 4.1.2 on 2022-11-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_slug_news_price_news_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
