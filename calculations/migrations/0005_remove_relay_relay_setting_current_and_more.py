# Generated by Django 5.1.6 on 2025-02-25 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculations', '0004_relay_protected_equipment_alter_relay_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relay',
            name='relay_setting_current',
        ),
        migrations.RemoveField(
            model_name='relay',
            name='time_multiplier_setting',
        ),
    ]
