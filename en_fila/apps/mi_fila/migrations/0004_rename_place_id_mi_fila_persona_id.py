# Generated by Django 3.2.6 on 2021-11-02 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_fila', '0003_alter_mi_fila_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mi_fila',
            old_name='place_id',
            new_name='persona_id',
        ),
    ]
