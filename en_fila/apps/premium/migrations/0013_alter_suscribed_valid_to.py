# Generated by Django 3.2.6 on 2021-11-02 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0012_auto_20211028_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscribed',
            name='valid_to',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 2, 18, 33, 52, 955937)),
        ),
    ]
