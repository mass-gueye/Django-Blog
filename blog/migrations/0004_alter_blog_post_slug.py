# Generated by Django 3.2.3 on 2021-07-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
