# Generated by Django 5.0 on 2023-12-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSend', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(default=0)),
                ('message', models.CharField(max_length=1000)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]