# Generated by Django 5.1.6 on 2025-03-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transformer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('kva_rating', models.IntegerField()),
                ('primary_voltage', models.FloatField()),
                ('secondary_voltage', models.FloatField()),
                ('impedance', models.FloatField()),
                ('phase_type', models.CharField(choices=[('single', 'Single-Phase'), ('three', 'Three-Phase')], default='three', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('kva_rating', models.IntegerField()),
                ('voltage_rating', models.FloatField()),
                ('impedance', models.FloatField()),
                ('length', models.FloatField(default=0)),
                ('r_per_km', models.FloatField(default=0)),
                ('x_per_km', models.FloatField(default=0)),
                ('phase_type', models.CharField(choices=[('single', 'Single-Phase'), ('three', 'Three-Phase')], default='three', max_length=6)),
            ],
        ),
    ]
