# Generated by Django 2.1.4 on 2019-06-03 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogue', '0004_blog_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
