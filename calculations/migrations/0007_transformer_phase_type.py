# Generated by Django 5.1.6 on 2025-02-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculations', '0006_transmissionline_relay_current_setting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformer',
            name='phase_type',
            field=models.CharField(choices=[('single', 'Single-Phase'), ('three', 'Three-Phase')], default='three', max_length=6),
        ),
    ]
