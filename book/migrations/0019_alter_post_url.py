# Generated by Django 4.1.7 on 2023-03-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
