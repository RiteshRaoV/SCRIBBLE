# Generated by Django 4.2.14 on 2024-07-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_APP', '0003_alter_blog_blog_content_alter_blog_blog_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]