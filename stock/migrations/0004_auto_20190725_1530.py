# Generated by Django 2.0.7 on 2019-07-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20190725_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='tAvailableShares',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='tMarketCap',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='tRequirement',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='tTotalShares',
            field=models.BigIntegerField(default=0),
        ),
    ]
