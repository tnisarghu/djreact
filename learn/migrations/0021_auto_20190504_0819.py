# Generated by Django 2.2 on 2019-05-04 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0020_auto_20190504_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnname',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Learn'),
        ),
    ]
