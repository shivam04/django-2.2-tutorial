# Generated by Django 2.2 on 2020-08-09 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200809_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['pk', '-publish_date', '-updated', '-timestamp']},
        ),
    ]
