# Generated by Django 2.1.4 on 2019-06-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogue', '0013_auto_20190605_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_post',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blogue.Tag'),
        ),
    ]