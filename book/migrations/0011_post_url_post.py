# Generated by Django 4.1.7 on 2023-03-21 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_remove_post_url_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_post',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
