# Generated by Django 2.2 on 2019-05-01 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0013_auto_20190501_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnname',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Learn'),
        ),
    ]