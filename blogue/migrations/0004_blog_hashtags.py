# Generated by Django 2.1.4 on 2019-06-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogue', '0003_auto_20190603_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hashtags',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
    ]
