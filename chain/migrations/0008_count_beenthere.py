# Generated by Django 2.0.5 on 2018-10-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0007_auto_20181011_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='beenThere',
            field=models.BooleanField(default=False),
        ),
    ]