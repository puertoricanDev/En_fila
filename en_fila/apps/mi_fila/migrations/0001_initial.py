# Generated by Django 3.2.6 on 2021-10-22 12:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('premium', '0003_alter_suscribed_valid_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='mi_fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_places', models.CharField(max_length=45)),
                ('persona', models.CharField(max_length=50)),
                ('llegada', models.DateTimeField(default=django.utils.timezone.now)),
                ('posicion', models.PositiveIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='premium.suscribed')),
            ],
        ),
    ]