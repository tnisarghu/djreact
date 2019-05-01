# Generated by Django 2.2 on 2019-05-01 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0015_auto_20190501_1610'),
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
            field=models.CharField(blank='True', default='Pathology', max_length=25, null='True'),
        ),
        migrations.AlterField(
            model_name='learnname',
            name='system',
            field=models.CharField(blank='True', default='Renal', max_length=45, null='True'),
        ),
    ]
