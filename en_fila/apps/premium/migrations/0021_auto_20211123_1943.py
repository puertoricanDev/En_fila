# Generated by Django 3.2.6 on 2021-11-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0020_auto_20211123_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscribed',
            name='valid_to',
        ),
        migrations.AlterField(
            model_name='suscribed',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
