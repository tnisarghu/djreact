# Generated by Django 2.2 on 2019-04-23 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190423_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
