# Generated by Django 2.2 on 2019-04-30 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0009_auto_20190430_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnname',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.Learn'),
        ),
        migrations.AlterField(
            model_name='learnname',
            name='subject',
            field=models.CharField(blank='True', max_length=25, null='True'),
        ),
    ]