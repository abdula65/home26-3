# Generated by Django 4.1.7 on 2023-03-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(null=True),
        ),
    ]