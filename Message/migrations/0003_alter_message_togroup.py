# Generated by Django 5.0 on 2024-01-01 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_initial'),
        ('Message', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='toGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Group.group'),
        ),
    ]
